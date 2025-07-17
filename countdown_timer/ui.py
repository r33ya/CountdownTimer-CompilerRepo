from Cocoa import *
from AppKit import *

class CountdownUI(NSObject):
    def __init__(self, countdown, sound_manager):
        super().__init__()
        self.countdown = countdown
        self.sound_manager = sound_manager
        self.window = None
        self.time_label = None
        self.start_button = None
        self.choose_sound_button = None

    def create_window(self):
        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            ((100, 100), (400, 300)),
            NSWindowStyleMaskTitled | NSWindowStyleMaskClosable | NSWindowStyleMaskResizable,
            NSBackingStoreBuffered,
            False
        )
        self.window.setTitle_("倒计时工具")
        self.window.setBackgroundColor_(NSColor.colorWithRed_green_blue_alpha_(0.17, 0.19, 0.22, 1))
        self.window.makeKeyAndOrderFront_(None)

    def create_ui(self):
        self.time_label = NSTextField.alloc().initWithFrame_(((100, 200), (200, 40)))
        self.time_label.setEditable_(False)
        self.time_label.setBezeled_(False)
        self.time_label.setDrawsBackground_(False)
        self.time_label.setFont_(NSFont.fontWithName_size_("Helvetica Neue", 30))
        self.time_label.setTextColor_(NSColor.whiteColor())
        self.window.contentView().addSubview_(self.time_label)

        self.start_button = NSButton.alloc().initWithFrame_(((100, 120), (200, 40)))
        self.start_button.setTitle_("设置倒计时")
        self.start_button.setTarget_(self)
        self.start_button.setAction_("on_set_timer:")
        self.window.contentView().addSubview_(self.start_button)

        self.choose_sound_button = NSButton.alloc().initWithFrame_(((100, 50), (200, 40)))
        self.choose_sound_button.setTitle_("选择铃声")
        self.choose_sound_button.setTarget_(self)
        self.choose_sound_button.setAction_("on_choose_sound:")
        self.window.contentView().addSubview_(self.choose_sound_button)

    def on_set_timer_(self, sender):
        dialog = NSAlert.alloc().init()
        dialog.setMessageText_("请输入倒计时时长（秒）")
        input_field = NSTextField.alloc().initWithFrame_(((50, 40), (300, 40)))
        input_field.setStringValue_("")
        dialog.setAccessoryView_(input_field)
        dialog.addButtonWithTitle_("确定")
        dialog.addButtonWithTitle_("取消")

        response = dialog.runModal()
        if response == NSAlertFirstButtonReturn:
            try:
                seconds = int(input_field.stringValue())
                self.countdown.set_timer(seconds)
                self.update_time_display()
            except ValueError:
                self.show_error("请输入有效的数字")

    def on_choose_sound_(self, sender):
        dialog = NSOpenPanel.openPanel()
        dialog.setAllowedFileTypes_(["mp3", "wav"])
        dialog.setCanChooseFiles_(True)
        dialog.setCanChooseDirectories_(False)
        if dialog.runModal() == NSFileHandlingPanelOKButton:
            sound_file = dialog.URL().path()
            self.sound_manager.set_sound(sound_file)

    def update_time_display(self):
        if self.countdown.time_left > 0:
            minutes, seconds = divmod(self.countdown.time_left, 60)
            self.time_label.setStringValue_(f"{minutes:02}:{seconds:02}")
            self.performSelector_withObject_afterDelay_(
                "update_time_display", None, 1.0
            )
        else:
            self.time_label.setStringValue_("00:00")

    def show_error(self, message):
        alert = NSAlert.alloc().init()
        alert.setMessageText_(message)
        alert.runModal()
