class WashingMachine:
    def __init__(self, start: bool, open_door: bool, close_door: bool, wash: bool, initial_time: int):
        self.start = start
        self.open = open_door
        self.close = close_door
        self.wash = wash
        self.__time = initial_time  # Private attribute
        self.__stop = False         # Private attribute
        self.ringtone = "Standard Beep"

    def set_time(self, new_time: int):
        if new_time >= 0:
            self.__time = new_time
            print(f"Time set to {self.__time} minutes.")

    def stop_machine(self):
        self.__stop = True
        self.start = False
        print("Machine stopped. Start property set to False.")

    def ring_when_finished(self) -> str:
        if self.__time == 0 and self.start:
            return f"[{self.ringtone}] Ring! The machine is done washing!"
        return f"Machine running. {self.__time} mins remaining."

    def beep_when_button_pressed(self) -> str:
        return "Beep!"

    def select_ringtone(self, ringtone_name: str) -> str:
        self.ringtone = ringtone_name
        return f"Ringtone set to: {self.ringtone}"

    def get_time(self) -> int:
        return self.__time

if __name__ == "__main__":
    machine1 = WashingMachine(start=True, open_door=False, close_door=True, wash=True, initial_time=30)
    machine2 = WashingMachine(start=False, open_door=True, close_door=False, wash=False, initial_time=45)

    print("--- BEFORE ---")
    print(f"Machine 1 -> Start: {machine1.start}, Time: {machine1.get_time()} mins")
    print(f"Machine 2 -> Start: {machine2.start}, Time: {machine2.get_time()} mins")

    print("\nExecuting action on Machine 1 only...")
    machine1.set_time(10)

    print("\n--- AFTER ---")
    print(f"Machine 1 -> Start: {machine1.start}, Time: {machine1.get_time()} mins")
    print(f"Machine 2 -> Start: {machine2.start}, Time: {machine2.get_time()} mins")