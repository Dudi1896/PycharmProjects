from Lab10.emp import ProductionWorker


def main():
    while True:
        shift_code = int(input("Enter shift number: "))
        pay_rate = float(input("Enter Pay rate: $ "))
        name_of_emp = str(input("Enter Employee Name: "))
        id_of_emp = str(input("Enter Employee ID: "))

        new_worker = ProductionWorker(shift_code, pay_rate, name_of_emp, id_of_emp)

        new_worker.set_shift_num(shift_code)
        new_worker.set_hourly_pay_rate(pay_rate)
        new_worker.set_emp_name(name_of_emp)
        new_worker.set_emp_number(id_of_emp)

        if shift_code == 2:
            new_worker.set_hourly_pay_rate(pay_rate + 0.50)
        elif shift_code == 3:
            new_worker.set_hourly_pay_rate(pay_rate + 1.00)

        print(f"\n\n|-------------Worker Details-------------------|")
        print(f"shift number: # {new_worker.get_shift_num()} ")
        print(f"Wage per hour: $ {new_worker.get_hourly_pay_rate():.2f}")
        print(f"Employee Name: {new_worker.get_emp_name()} ")
        print(f"Employee ID: {new_worker.get_emp_number()} ")

        replay_code = input("Try again? (y/n): ")
        if replay_code.lower() != "y":
            break


if __name__ == '__main__':
    main()
