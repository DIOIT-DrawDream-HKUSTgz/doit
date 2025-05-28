class ControllersManager:
    """控制器管理器 - 统一管理所有控制器"""
    
    def __init__(self):
        self.controllers = {}  # 存储所有控制器实例
        
    def register_controller(self, name, controller):
        """注册一个控制器实例"""
        if name in self.controllers:
            # 如果已经存在同名控制器，转为列表存储多个
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
        # 遍历所有控制器，查找包含该方法的控制器
        for controller_key, controller in self.controllers.items():
            # 如果是控制器列表，则遍历列表
            if isinstance(controller, list):
                for single_controller in controller:
                    if hasattr(single_controller, name):
                        return getattr(single_controller, name)
            else:
                # 单个控制器
                if hasattr(controller, name):
                    return getattr(controller, name)
                
        # 如果找不到方法，抛出AttributeError
        raise AttributeError(f"没有找到方法: {name}")
