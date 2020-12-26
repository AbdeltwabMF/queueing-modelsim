from tkinter import *
from tkinter.messagebox import *

from Plots import *
from Stochastic import *
from Deterministic import *


class Windows:
    def __init__(self, master):
        # --- Frames --- #
        label_frame1 = LabelFrame(master, text="Models", font=('Ubuntu', 10), fg="#0033ff")
        label_frame1.grid(row=0, column=0, pady=10, padx=0, columnspan=2)

        label_frame2 = LabelFrame(master, text="Inputs", font=('Ubuntu', 10), fg="#0033ff")
        label_frame2.grid(row=1, column=0, pady=10, padx=10, columnspan=2)

        label_frame3 = LabelFrame(master, text="Functions", font=('Ubuntu', 10), fg="#0033ff")
        label_frame3.grid(row=2, column=0, pady=10, padx=0, columnspan=2)

        frame1 = Frame(label_frame2)
        frame1.grid(row=0, column=0, pady=10, padx=10)

        frame2 = Frame(label_frame2)
        frame2.grid(row=0, column=1, pady=10, padx=10)

        frame3 = Frame(label_frame2)
        frame3.grid(row=1, column=0, pady=10, padx=0, columnspan=2)

        frame5 = Frame(label_frame3)
        frame5.grid(row=0, column=0, pady=10, padx=0)

        frame6 = Frame(label_frame3)
        frame6.grid(row=0, column=1, pady=10, padx=0)

        # --- Buttons --- #
        self.Quit = Button(frame5, text="Quit", font=('Ubuntu', 16), fg="red", command=self.exit_program)
        self.Quit.grid(row=0, column=0, sticky=W, pady=0, padx=86)

        self.Calculate = Button(frame6, text="Calculate", font=('Ubuntu', 16), fg="green", command=self.radio_event)
        self.Calculate.grid(row=0, column=0, sticky=W, pady=0, padx=86)

        # --- Radio Buttons --- #
        self.rad_values = IntVar()

        self.DD1K = Radiobutton(label_frame1, text="D/D/1/K", font=('Ubuntu', 16), fg="#cc0033", value=1, variable=self.rad_values, indicatoron=False)
        self.DD1K.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.MM1 = Radiobutton(label_frame1, text="M/M/1", font=('Ubuntu', 16), fg="#3300cc", value=2, variable=self.rad_values, indicatoron=False)
        self.MM1.grid(row=0, column=1, sticky=W, pady=10, padx=10)

        self.MM1K = Radiobutton(label_frame1, text="M/M/1/K", font=('Ubuntu', 16), fg="#ff9933", value=3, variable=self.rad_values, indicatoron=False)
        self.MM1K.grid(row=0, column=2, sticky=W, pady=10, padx=10)

        self.MMc = Radiobutton(label_frame1, text="M/M/C", font=('Ubuntu', 16), fg="#006666", value=4, variable=self.rad_values, indicatoron=False)
        self.MMc.grid(row=0, column=3, sticky=W, pady=10, padx=10)

        self.MMcK = Radiobutton(label_frame1, text="M/M/C/K", font=('Ubuntu', 16), fg="#000033", value=5, variable=self.rad_values, indicatoron=False)
        self.MMcK.grid(row=0, column=4, sticky=W, pady=10, padx=10)

        # --- Labels --- #
        self.__lambda = Label(frame1, text="Arrival rate(λ):", font=('Ubuntu', 16))
        self.__lambda.grid(row=0, column=0, sticky=W)

        self.__mu = Label(frame1, text="Service rate(μ):", font=('Ubuntu', 16))
        self.__mu.grid(row=1, column=0, sticky=W)

        self.__k = Label(frame2, text="Queue Capacity(K):", font=('Ubuntu', 16))
        self.__k.grid(row=0, column=0, sticky=W)

        self.__c = Label(frame2, text="Servers(C):", font=('Ubuntu', 16))
        self.__c.grid(row=1, column=0, sticky=W)

        self.__M = Label(frame3, text="Initial Customers(M):", font=('Ubuntu', 16))
        self.__M.grid(row=0, column=0, sticky=W)

        # --- Entries --- #
        self.__elambda = Entry(frame1, bd=2, font=('Ubuntu', 10))
        self.__elambda.grid(row=0, column=1)

        self.__emu = Entry(frame1, bd=2, font=('Ubuntu', 10), justify=LEFT)
        self.__emu.grid(row=1, column=1)

        self.__ek = Entry(frame2, bd=2, font=('Ubuntu', 10))
        self.__ek.grid(row=0, column=1)

        self.__ec = Entry(frame2, bd=2, font=('Ubuntu', 10))
        self.__ec.grid(row=1, column=1)

        self.__eM = Entry(frame3, bd=2, font=('Ubuntu', 10))
        self.__eM.grid(row=0, column=1)

    @staticmethod
    def exit_program():
        if askquestion(title='Quit?', message='Do you really want to quit?') == 'yes':
            quit()

    def radio_event(self):
        radio_selected = self.rad_values.get()

        if radio_selected == 1:
            try:
                dd1k = DD1K(self.__elambda.get(), self.__emu.get(), self.__ek.get(), self.__eM.get())
                Plots.plot_system_size_per_time(dd1k)

            except SyntaxError:
                showwarning(title="Warning", message="Please, enter a real value for λ, μ, K and M")
            except ZeroDivisionError as zde:
                showwarning(title="Warning", message=f"{zde}")
            except Exception as e:
                showwarning(title="Warning", message=f"{e}")

        elif radio_selected == 2:
            try:
                mm1 = MM1(self.__elambda.get(), self.__emu.get())
                answer = Tk()
                answer.title("M/M/1")

                label_frame_l = LabelFrame(answer, text="Average Customers in System", font=('Ubuntu', 10), fg="#ff6600")
                label_frame_l.grid(row=0, column=0, sticky=W, padx=10, pady=10)

                capital_l_left = Label(label_frame_l, text="L =", font=('Ubuntu', 16), fg="#ff6600")
                capital_l_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_l_right = Label(label_frame_l, text=f"{mm1.capital_l()} Customers", font=('Ubuntu', 16), fg="#ff6600")
                capital_l_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_lq = LabelFrame(answer, text="Average Customers in Queue", font=('Ubuntu', 10), fg="#333333")
                label_frame_lq.grid(row=1, column=0, sticky=W, padx=10, pady=10)

                capital_lq_left = Label(label_frame_lq, text="Lq =", font=('Ubuntu', 16), fg="#333333")
                capital_lq_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_lq_right = Label(label_frame_lq, text=f"{mm1.capital_lq()} Customers", font=('Ubuntu', 16), fg="#333333")
                capital_lq_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_w = LabelFrame(answer, text="Average Time Spent in System", font=('Ubuntu', 10), fg="#ff00ff")
                label_frame_w.grid(row=2, column=0, sticky=W, padx=10, pady=10)

                capital_w_left = Label(label_frame_w, text="W =", font=('Ubuntu', 16), fg="#ff00ff")
                capital_w_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_w_right = Label(label_frame_w, text=f"{mm1.capital_w()} Minutes", font=('Ubuntu', 16), fg="#ff00ff")
                capital_w_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_wq = LabelFrame(answer, text="Average Time Waiting in Line", font=('Ubuntu', 10), fg="#003333")
                label_frame_wq.grid(row=3, column=0, sticky=W, padx=10, pady=10)

                capital_wq_left = Label(label_frame_wq, text="Wq =", font=('Ubuntu', 16), fg="#003333")
                capital_wq_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_wq_right = Label(label_frame_wq, text=f"{mm1.capital_wq()} Minutes", font=('Ubuntu', 16), fg="#003333")
                capital_wq_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_rho = LabelFrame(answer, text="Server Utilization", font=('Ubuntu', 10), fg="#0000ff")
                label_frame_rho.grid(row=4, column=0, sticky=W, padx=10, pady=10)

                capital_rho_left = Label(label_frame_rho, text="ρ =", font=('Ubuntu', 16), fg="#0000ff")
                capital_rho_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_rho_right = Label(label_frame_rho, text=f"{mm1.get_rho()}", font=('Ubuntu', 16), fg="#0000ff")
                capital_rho_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                answer.mainloop()

            except SyntaxError:
                showwarning(title="Warning", message="Please, enter a real value for λ and μ")
            except ZeroDivisionError as zde:
                showwarning(title="Warning", message=f"{zde}")
            except Exception as e:
                showwarning(title="Warning", message=f"{e}")

        elif radio_selected == 3:
            try:
                mm1k = MM1K(self.__elambda.get(), self.__emu.get(), self.__ek.get())
                answer = Tk()
                answer.title("M/M/1/K")

                label_frame_l = LabelFrame(answer, text="Average Customers in System", font=('Ubuntu', 10), fg="#ff6600")
                label_frame_l.grid(row=0, column=0, sticky=W, padx=10, pady=10)

                capital_l_left = Label(label_frame_l, text="L =", font=('Ubuntu', 16), fg="#ff6600")
                capital_l_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_l_right = Label(label_frame_l, text=f"{mm1k.capital_l()} Customers", font=('Ubuntu', 16), fg="#ff6600")
                capital_l_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_lq = LabelFrame(answer, text="Average Customers in Queue", font=('Ubuntu', 10), fg="#333333")
                label_frame_lq.grid(row=1, column=0, sticky=W, padx=10, pady=10)

                capital_lq_left = Label(label_frame_lq, text="Lq =", font=('Ubuntu', 16), fg="#333333")
                capital_lq_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_lq_right = Label(label_frame_lq, text=f"{mm1k.capital_lq()} Customers", font=('Ubuntu', 16), fg="#333333")
                capital_lq_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_w = LabelFrame(answer, text="Average Time Spent in System", font=('Ubuntu', 10), fg="#ff00ff")
                label_frame_w.grid(row=2, column=0, sticky=W, padx=10, pady=10)

                capital_w_left = Label(label_frame_w, text="W =", font=('Ubuntu', 16), fg="#ff00ff")
                capital_w_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_w_right = Label(label_frame_w, text=f"{mm1k.capital_w()} Minutes", font=('Ubuntu', 16), fg="#ff00ff")
                capital_w_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_wq = LabelFrame(answer, text="Average Time Waiting in Line", font=('Ubuntu', 10), fg="#003333")
                label_frame_wq.grid(row=3, column=0, sticky=W, padx=10, pady=10)

                capital_wq_left = Label(label_frame_wq, text="Wq =", font=('Ubuntu', 16), fg="#003333")
                capital_wq_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_wq_right = Label(label_frame_wq, text=f"{mm1k.capital_wq()} Minutes", font=('Ubuntu', 16), fg="#003333")
                capital_wq_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_rho = LabelFrame(answer, text="Server Utilization", font=('Ubuntu', 10), fg="#0000ff")
                label_frame_rho.grid(row=4, column=0, sticky=W, padx=10, pady=10)

                capital_rho_left = Label(label_frame_rho, text="ρ =", font=('Ubuntu', 16), fg="#0000ff")
                capital_rho_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_rho_right = Label(label_frame_rho, text=f"{mm1k.get_rho()}", font=('Ubuntu', 16), fg="#0000ff")
                capital_rho_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                answer.mainloop()

            except SyntaxError:
                showwarning(title="Warning", message="Please, enter a real value for λ, μ and K")
            except ZeroDivisionError as zde:
                showwarning(title="Warning", message=f"{zde}")
            except Exception as e:
                showwarning(title="Warning", message=f"{e}")

        elif radio_selected == 4:
            try:
                mmc = MMc(self.__elambda.get(), self.__emu.get(), self.__ec.get())
                answer = Tk()
                answer.title("M/M/C")

                label_frame_l = LabelFrame(answer, text="Average Customers in System", font=('Ubuntu', 10), fg="#ff6600")
                label_frame_l.grid(row=0, column=0, sticky=W, padx=10, pady=10)

                capital_l_left = Label(label_frame_l, text="L =", font=('Ubuntu', 16), fg="#ff6600")
                capital_l_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_l_right = Label(label_frame_l, text=f"{mmc.capital_l()} Customers", font=('Ubuntu', 16), fg="#ff6600")
                capital_l_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_lq = LabelFrame(answer, text="Average Customers in Queue", font=('Ubuntu', 10), fg="#333333")
                label_frame_lq.grid(row=1, column=0, sticky=W, padx=10, pady=10)

                capital_lq_left = Label(label_frame_lq, text="Lq =", font=('Ubuntu', 16), fg="#333333")
                capital_lq_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_lq_right = Label(label_frame_lq, text=f"{mmc.capital_lq()} Customers", font=('Ubuntu', 16), fg="#333333")
                capital_lq_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_w = LabelFrame(answer, text="Average Time Spent in System", font=('Ubuntu', 10), fg="#ff00ff")
                label_frame_w.grid(row=2, column=0, sticky=W, padx=10, pady=10)

                capital_w_left = Label(label_frame_w, text="W =", font=('Ubuntu', 16), fg="#ff00ff")
                capital_w_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_w_right = Label(label_frame_w, text=f"{mmc.capital_w()} Minutes", font=('Ubuntu', 16), fg="#ff00ff")
                capital_w_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_wq = LabelFrame(answer, text="Average Time Waiting in Line", font=('Ubuntu', 10), fg="#003333")
                label_frame_wq.grid(row=3, column=0, sticky=W, padx=10, pady=10)

                capital_wq_left = Label(label_frame_wq, text="Wq =", font=('Ubuntu', 16), fg="#003333")
                capital_wq_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_wq_right = Label(label_frame_wq, text=f"{mmc.capital_wq()} Minutes", font=('Ubuntu', 16), fg="#003333")
                capital_wq_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_rho = LabelFrame(answer, text="Server Utilization", font=('Ubuntu', 10), fg="#0000ff")
                label_frame_rho.grid(row=4, column=0, sticky=W, padx=10, pady=10)

                capital_rho_left = Label(label_frame_rho, text="ρ =", font=('Ubuntu', 16), fg="#0000ff")
                capital_rho_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_rho_right = Label(label_frame_rho, text=f"{mmc.get_rho()}", font=('Ubuntu', 16), fg="#0000ff")
                capital_rho_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                answer.mainloop()

            except SyntaxError:
                showwarning(title="Warning", message="Please, enter a real value for λ, μ and C")
            except ZeroDivisionError as zde:
                showwarning(title="Warning", message=f"{zde}")
            except Exception as e:
                showwarning(title="Warning", message=f"{e}")

        elif radio_selected == 5:
            try:
                mmck = MMcK(self.__elambda.get(), self.__emu.get(), self.__ec.get(), self.__ek.get())
                answer = Tk()
                answer.title("M/M/C/K")

                label_frame_l = LabelFrame(answer, text="Average Customers in System", font=('Ubuntu', 10), fg="#ff6600")
                label_frame_l.grid(row=0, column=0, sticky=W, padx=10, pady=10)

                capital_l_left = Label(label_frame_l, text="L =", font=('Ubuntu', 16), fg="#ff6600")
                capital_l_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_l_right = Label(label_frame_l, text=f"{mmck.capital_l()} Customers", font=('Ubuntu', 16), fg="#ff6600")
                capital_l_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_lq = LabelFrame(answer, text="Average Customers in Queue", font=('Ubuntu', 10), fg="#333333")
                label_frame_lq.grid(row=1, column=0, sticky=W, padx=10, pady=10)

                capital_lq_left = Label(label_frame_lq, text="Lq =", font=('Ubuntu', 16), fg="#333333")
                capital_lq_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_lq_right = Label(label_frame_lq, text=f"{mmck.capital_lq()} Customers", font=('Ubuntu', 16), fg="#333333")
                capital_lq_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_w = LabelFrame(answer, text="Average Time Spent in System", font=('Ubuntu', 10), fg="#ff00ff")
                label_frame_w.grid(row=2, column=0, sticky=W, padx=10, pady=10)

                capital_w_left = Label(label_frame_w, text="W =", font=('Ubuntu', 16), fg="#ff00ff")
                capital_w_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_w_right = Label(label_frame_w, text=f"{mmck.capital_w()} Minutes", font=('Ubuntu', 16), fg="#ff00ff")
                capital_w_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_wq = LabelFrame(answer, text="Average Time Waiting in Line", font=('Ubuntu', 10), fg="#003333")
                label_frame_wq.grid(row=3, column=0, sticky=W, padx=10, pady=10)

                capital_wq_left = Label(label_frame_wq, text="Wq =", font=('Ubuntu', 16), fg="#003333")
                capital_wq_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_wq_right = Label(label_frame_wq, text=f"{mmck.capital_wq()} Minutes", font=('Ubuntu', 16), fg="#003333")
                capital_wq_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                label_frame_rho = LabelFrame(answer, text="Server Utilization", font=('Ubuntu', 10), fg="#0000ff")
                label_frame_rho.grid(row=4, column=0, sticky=W, padx=10, pady=10)

                capital_rho_left = Label(label_frame_rho, text="ρ =", font=('Ubuntu', 16), fg="#0000ff")
                capital_rho_left.grid(row=0, column=0, sticky=W, padx=10, pady=5)

                capital_rho_right = Label(label_frame_rho, text=f"{mmck.get_rho()}", font=('Ubuntu', 16), fg="#0000ff")
                capital_rho_right.grid(row=0, column=1, sticky=W, padx=10, pady=5)

                answer.mainloop()

            except SyntaxError:
                showwarning(title="Warning", message="Please, enter a real value for λ, μ, C and K")
            except ZeroDivisionError as zde:
                showwarning(title="Warning", message=f"{zde}")
            except Exception as e:
                showwarning(title="Warning", message=f"{e}")

        else:
            showwarning(title="Warning", message="Please, Choose a Model!!")
