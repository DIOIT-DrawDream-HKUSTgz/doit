import readline

class MenuBase:
    """菜单基类，提供命令解析和自动补全基础功能"""
    
    def __init__(self, name, prompt, commands_dict, parent=None):
        self.name = name
        self.prompt = prompt
        self.commands_dict = commands_dict  # {命令名: (处理函数, 帮助文本)}
        self.parent = parent
        self.command_names = list(commands_dict.keys()) + ['help', 'quit', 'back']
        
    def setup_completer(self):
        """设置当前菜单的自动补全"""
        readline.set_completer(self._create_completer())
        readline.parse_and_bind('tab: complete')
        
    def _create_completer(self):
        """创建自动补全函数"""
        def completer(text, state):
            matches = [cmd for cmd in self.command_names if cmd.startswith(text.lower())]
            return matches[state] if state < len(matches) else None
        return completer
    
    def _setup_param_completer(self, options):
        """设置参数的自动补全选项"""
        def completer(text, state):
            matches = [opt for opt in options if opt.startswith(text.lower())]
            return matches[state] if state < len(matches) else None
            
        readline.set_completer(completer)
    
    def handle_input(self):
        """处理用户输入"""
        self.setup_completer()
        while True:
            try:
                cmd = input(self.prompt).strip().lower()
                if cmd == 'help':
                    self.show_help()
                elif cmd == 'quit':
                    return False
                elif cmd == 'back' and self.parent is not None:
                    return True
                elif cmd in self.commands_dict:
                    handler, _ = self.commands_dict[cmd]
                    result = handler()
                    if result is False:  # 命令处理返回False表示退出程序
                        return False
                else:
                    print("无效的命令，请重新输入")
            except (KeyboardInterrupt, EOFError):
                print("\n操作被中断")
                return False
                
    def show_help(self):
        """显示帮助信息"""
        print(f"\n==== {self.name} 帮助 ====")
        for cmd, (_, help_text) in self.commands_dict.items():
            print(f"  {cmd:<15} - {help_text}")
        print("  help            - 显示此帮助")
        if self.parent is not None:
            print("  back            - 返回上级菜单")
        print("  quit            - 退出程序")