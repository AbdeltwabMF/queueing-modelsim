from tkinter import *
from tkinter.messagebox import *
from Plots import *
from Stochastic import *
from src.Deterministic import *


class Windows:
    def __init__(self, master):
        # --- Frames --- #
        label_frame1 = LabelFrame(master, text="Models", font=('Ubuntu', 10), fg="#0033ff")
        label_frame1.grid(row=0, column=0, pady=10, padx=10, rowspan=2)

        label_frame2 = LabelFrame(master, text="Inputs", font=('Ubuntu', 10), fg="#0033ff")
        label_frame2.grid(row=0, column=1, pady=10, padx=10)

        label_frame3 = LabelFrame(master, text="", font=('Ubuntu', 10), fg="#0033ff")
        label_frame3.grid(row=1, column=1, pady=10, padx=10)

        frame1 = Frame(label_frame2)
        frame1.grid(row=0, column=0, pady=5, padx=5, sticky=W)

        frame2 = Frame(label_frame2)
        frame2.grid(row=0, column=1, pady=5, padx=5, sticky=W)

        frame5 = Frame(label_frame3)
        frame5.grid(row=0, column=0, pady=5, padx=10)

        frame6 = Frame(label_frame3)
        frame6.grid(row=0, column=1, pady=5, padx=10)

        # --- Buttons --- #
        self.Quit_img = PhotoImage(file="Img/button_quit.png")
        self.Calculate_img = PhotoImage(file="Img/button_calculate.png")

        self.Quit = Button(frame5, image=self.Quit_img, command=self.exit_program, borderwidth=0)
        self.Quit.grid(row=0, column=0, sticky=W, pady=3, padx=16)

        self.Calculate = Button(frame6, image=self.Calculate_img, command=self.radio_event, borderwidth=0)
        self.Calculate.grid(row=0, column=0, sticky=W, pady=3, padx=16)

        # --- Radio Buttons --- #
        self.rad_values = IntVar()

        self.DD1K_img = PhotoImage(file="Img/button_d-d-k.png")
        self.MM1_img = PhotoImage(file="Img/button_m-m-1.png")
        self.MM1K_img = PhotoImage(file="Img/button_m-m-k.png")
        self.MMc_img = PhotoImage(file="Img/button_m-m-c.png")
        self.MMcK_img = PhotoImage(file="Img/button_m-m-c-k.png")

        # indicatoron = False
        self.DD1K = Radiobutton(label_frame1, image=self.DD1K_img, value=1, variable=self.rad_values, borderwidth=0, command=self.rad_dd1k)
        self.DD1K.grid(row=0, column=0, sticky=W, pady=5, padx=10)

        self.MM1 = Radiobutton(label_frame1, image=self.MM1_img, value=2, variable=self.rad_values, borderwidth=0, command=self.rad_mm1)
        self.MM1.grid(row=1, column=0, sticky=W, pady=0, padx=10)

        self.MM1K = Radiobutton(label_frame1, image=self.MM1K_img, value=3, variable=self.rad_values, borderwidth=0, command=self.rad_mm1k)
        self.MM1K.grid(row=2, column=0, sticky=W, pady=5, padx=10)

        self.MMc = Radiobutton(label_frame1, image=self.MMc_img, value=4, variable=self.rad_values, borderwidth=0, command=self.rad_mmc)
        self.MMc.grid(row=3, column=0, sticky=W, pady=0, padx=10)

        self.MMcK = Radiobutton(label_frame1, image=self.MMcK_img, value=5, variable=self.rad_values, borderwidth=0, command=self.rad_mmck)
        self.MMcK.grid(row=4, column=0, sticky=W, pady=5, padx=10)

        # --- Labels --- #
        self.__lambda = Label(frame1, text="Arrival rate(λ):", font=('Ubuntu', 16))
        self.__lambda.grid(row=0, column=0, sticky=W, pady=0, padx=5)

        self.__mu = Label(frame1, text="Service rate(μ):", font=('Ubuntu', 16))
        self.__mu.grid(row=1, column=0, sticky=W, pady=5, padx=5)

        self.__k = Label(frame1, text="Queue Capacity(K):", font=('Ubuntu', 16))
        self.__k.grid(row=2, column=0, sticky=W, pady=0, padx=5)

        self.__c = Label(frame1, text="Servers(C):", font=('Ubuntu', 16))
        self.__c.grid(row=3, column=0, sticky=W, pady=5, padx=5)

        self.__M = Label(frame1, text="Initial Customers(M):", font=('Ubuntu', 16))
        self.__M.grid(row=4, column=0, sticky=W, pady=0, padx=5)

        # --- Entries --- #
        self.__elambda = Entry(frame2, bd=2, font=('Ubuntu', 10))
        self.__elambda.grid(row=0, column=1, sticky=W, pady=5, padx=5)

        self.__emu = Entry(frame2, bd=2, font=('Ubuntu', 10), justify=LEFT)
        self.__emu.grid(row=1, column=1, sticky=W, pady=5, padx=5)

        self.__ek = Entry(frame2, bd=2, font=('Ubuntu', 10))
        self.__ek.grid(row=2, column=1, sticky=W, pady=5, padx=5)

        self.__ec = Entry(frame2, bd=2, font=('Ubuntu', 10))
        self.__ec.grid(row=3, column=1, sticky=W, pady=5, padx=5)

        self.__eM = Entry(frame2, bd=2, font=('Ubuntu', 10))
        self.__eM.grid(row=4, column=1, sticky=W, pady=5, padx=5)

    @staticmethod
    def exit_program():
        if askquestion(title='Quit?', message='Do you really want to quit?') == 'yes':
            exit()

    def rad_dd1k(self):
        self.__elambda.configure(state="normal")
        self.__emu.configure(state="normal")
        self.__ek.configure(state="normal")
        self.__ec.configure(state="disabled")
        self.__eM.configure(state="normal", text="0")

    def rad_mm1(self):
        self.__elambda.configure(state="normal")
        self.__emu.configure(state="normal")
        self.__ek.configure(state="disabled")
        self.__ec.configure(state="disabled")
        self.__eM.configure(state="disabled", text="0")

    def rad_mm1k(self):
        self.__elambda.configure(state="normal")
        self.__emu.configure(state="normal")
        self.__ek.configure(state="normal")
        self.__ec.configure(state="disabled")
        self.__eM.configure(state="disabled", text="0")

    def rad_mmc(self):
        self.__elambda.configure(state="normal")
        self.__emu.configure(state="normal")
        self.__ek.configure(state="disabled")
        self.__ec.configure(state="normal")
        self.__eM.configure(state="disabled", text="0")

    def rad_mmck(self):
        self.__elambda.configure(state="normal")
        self.__emu.configure(state="normal")
        self.__ek.configure(state="normal")
        self.__ec.configure(state="normal")
        self.__eM.configure(state="disabled", text="0")

    def radio_event(self):
        radio_selected = self.rad_values.get()

        if radio_selected == 1:
            try:
                dd1k = DD1K(self.__elambda.get(), self.__emu.get(), self.__ek.get(), self.__eM.get())
                Plots.plot_system_size_per_time(dd1k)

                del dd1k

            except SyntaxError:
                showerror(title="Error", message="Please, enter a real value for λ, μ, K and M")
            except ZeroDivisionError as zde:
                showerror(title="Error", message=f"{zde}!")
            except Exception as e:
                showerror(title="Error", message=f"{e}!")

        elif radio_selected == 2:
            try:
                mm1 = MM1(self.__elambda.get(), self.__emu.get())

                try:
                    capital_l = mm1.capital_l()
                    capital_lq = mm1.capital_lq()
                    capital_w = mm1.capital_w()
                    capital_wq = mm1.capital_wq()
                    capital_rho = mm1.get_rho()
                except ZeroDivisionError as zde:
                    showerror(title="Error", message=f"{zde}!")
                except Exception as e:
                    showerror(title="Error", message=f"{e}!")
                else:
                    answer = Tk()
                    answer.title("M/M/1")

                    label_frame_l = LabelFrame(answer, text="Average Customers in System", font=('Ubuntu', 10), fg="#ff6600")
                    label_frame_l.grid(row=0, column=0, padx=10, pady=10)

                    capital_l_left = Label(label_frame_l, text="L =", font=('Ubuntu', 16), fg="#ff6600")
                    capital_l_left.grid(row=0, column=0, padx=10, pady=5)

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

                    del mm1
                    answer.mainloop()

            except SyntaxError:
                showerror(title="Error", message="Please, enter a real value for λ and μ")
            except ZeroDivisionError as zde:
                showerror(title="Error", message=f"{zde}!")
            except Exception as e:
                showerror(title="Error", message=f"{e}!")

        elif radio_selected == 3:
            try:
                mm1k = MM1K(self.__elambda.get(), self.__emu.get(), self.__ek.get())

                try:
                    capital_l = mm1k.capital_l()
                    capital_lq = mm1k.capital_lq()
                    capital_w = mm1k.capital_w()
                    capital_wq = mm1k.capital_wq()
                    capital_rho = mm1k.get_rho()
                except ZeroDivisionError as zde:
                    showerror(title="Error", message=f"{zde}!")
                except Exception as e:
                    showerror(title="Error", message=f"{e}!")
                else:
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

                    del mm1k
                    answer.mainloop()

            except SyntaxError:
                showerror(title="Error", message="Please, enter a real value for λ, μ and K")
            except ZeroDivisionError as zde:
                showerror(title="Error", message=f"{zde}!")
            except Exception as e:
                showerror(title="Error", message=f"{e}!")

        elif radio_selected == 4:
            try:
                mmc = MMc(self.__elambda.get(), self.__emu.get(), self.__ec.get())

                try:
                    capital_l = mmc.capital_l()
                    capital_lq = mmc.capital_lq()
                    capital_w = mmc.capital_w()
                    capital_wq = mmc.capital_wq()
                    capital_rho = mmc.get_rho()
                except ZeroDivisionError as zde:
                    showerror(title="Error", message=f"{zde}!")
                except Exception as e:
                    showerror(title="Error", message=f"{e}!")
                else:
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

                    del mmc
                    answer.mainloop()

            except SyntaxError:
                showerror(title="Error", message="Please, enter a real value for λ, μ and C")
            except ZeroDivisionError as zde:
                showerror(title="Error", message=f"{zde}!")
            except Exception as e:
                showerror(title="Error", message=f"{e}!")

        elif radio_selected == 5:
            try:
                mmck = MMcK(self.__elambda.get(), self.__emu.get(), self.__ec.get(), self.__ek.get())

                try:
                    capital_l = mmck.capital_l()
                    capital_lq = mmck.capital_lq()
                    capital_w = mmck.capital_w()
                    capital_wq = mmck.capital_wq()
                    capital_rho = mmck.get_rho()
                except ZeroDivisionError as zde:
                    showerror(title="Error", message=f"{zde}!")
                except Exception as e:
                    showerror(title="Error", message=f"{e}!")
                else:
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

                    del mmck
                    answer.mainloop()

            except SyntaxError:
                showerror(title="Error", message="Please, enter a real value for λ, μ, C and K")
            except ZeroDivisionError as zde:
                showerror(title="Error", message=f"{zde}")
            except Exception as e:
                showerror(title="Error", message=f"{e}")

        else:
            showwarning(title="Warning", message="Please, Choose a Model!!")
