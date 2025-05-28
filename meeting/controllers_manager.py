class ControllersManager:
    """控制器管理器 - 统一管理所有控制器"""
    
    def __init__(self):
        self.controllers = {}  # 存储所有控制器实例
        
    def register_controller(self, name, controller):
        """注册一个控制器实例"""
        if name in self.controllers:
            if not isinstance(self.controllers[name], list):
                self.controllers[name] = [self.controllers[name]]
            self.controllers[name].append(controller)
        else:
            self.controllers[name] = controller
        
    def get_controller(self, name):
        """获取指定名称的控制器"""
        return self.controllers.get(name)
    
    def __getattr__(self, name):
        """动态查找并调用控制器方法"""
        available_methods = []
        
        for controller_key, controller in self.controllers.items():
            if isinstance(controller, list):
                for single_controller in controller:
                    if hasattr(single_controller, name):
                        return getattr(single_controller, name)
                    available_methods.extend(dir(single_controller))
            else:
                if hasattr(controller, name):
                    return getattr(controller, name)
                available_methods.extend(dir(controller))

        public_methods = [m for m in set(available_methods) if not m.startswith('_')]
        similar_methods = [m for m in public_methods if name.lower() in m.lower()]

        error_msg = f"没有找到方法: {name}"
        if similar_methods:
            error_msg += f"\n可能的方法: {', '.join(similar_methods)}"
        
        raise AttributeError(error_msg)
