from engines.engine_parent import Engine

class SternmanEngine(Engine):
    warning_light_on:bool

    def __init__(self,warning_light_on):
        super().__init__()
        self.warning_light_on=warning_light_on

    def needs_service(self):
        return self.warning_light_on