class AppendMr:
    def __init__(self):
        self.info = []
        self.inside = []


    def append(self, qiymat):
        self.info.append(qiymat)


    def __enter__(self):
        self.inside = self.info.copy()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.info = self.inside
            print("Diqqat xatolik aniqlandi, ║asl holatiga qaytish║")
        else:
            print("Hozircha xatolik aniqlanmadi, ╙ o'zgarishlarni saqlash ╙")

def context_mr(func):
    def wrapper(*args, **kwargs):
        inside = args[0].info.copy()
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            args[0].info = inside
            print("Diqqat xatolik aniqlandi, ║asl holatiga qaytish║ ")
            raise exc
        else:
            print("Hozircha xatolar yo`q, ╢o`zgarishlarni saqlab olish╢ ")
    return wrapper


@context_mr
def append_qymt(manager, qiymat):
    manager.append(qiymat)


with AppendMr() as manager:
    manager.append(1)
    manager.append(2)
    manager.append(3)
    print(manager.info)
    raise ValueError("Nimadir xato ketyapti, xatolikni bartaraf eting!",)
print("Keyingi xolat con_mr:", manager.info)
manager = AppendMr()
append_qymt(manager, 4)
append_qymt(manager, 5)
append_qymt(manager, 6)
print(manager.info)
append_qymt(manager, 7)
print("Con_mr functiondan kegingi xol:", manager.info)