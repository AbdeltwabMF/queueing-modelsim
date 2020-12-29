from matplotlib import pyplot as plt


class Plots:
	@staticmethod
	def plot_system_size_per_time(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("t(s)", fontsize=16, loc="right", color="#ff0033")
		plt.ylabel("n(t)", fontsize=16, rotation=0, loc="top", color="#ff0033")
		plt.title("Customers in System per Second", fontsize=16, color="#220066")

		plt.ylim(0, dd1k.get_k() + dd1k.get_initial_customers() + 2)
		plt.xlim(0, 70)

		plt.step(range(len(dd1k.system_size_per_time)), dd1k.system_size_per_time, color="#cc0033", linewidth=3, label="Entities in System")

		plt.legend()
		plt.show()

	@staticmethod
	def plot_departure(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("Customer (n)", fontsize=16, loc="center", color="#ff0033")
		plt.ylabel("Time (s)", fontsize=16, rotation=90, loc="center", color="#ff0033")
		plt.title("Departure Time per Customer", fontsize=16, color="#220066")

		plt.ylim(0, max(dd1k.departures[:70]) + 2)
		plt.xlim(0, 70)

		plt.step(range(len(dd1k.departures)), dd1k.departures, color="#ffcc00", linewidth=3, label="Departure Time")

		plt.legend()
		plt.show()

	@staticmethod
	def plot_queue_time(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("Customer (n)", fontsize=16, loc="center", color="#ff0033")
		plt.ylabel("Time (s)", fontsize=16, rotation=90, loc="center", color="#ff0033")
		plt.title("Time Spent in Queue per Customer", fontsize=16, color="#220066")

		plt.ylim(0, max(dd1k.queue_time[:70]) + 2)
		plt.xlim(0, 70)

		plt.step(range(len(dd1k.queue_time)), dd1k.queue_time, color="#3399ff", linewidth=3, label="Waiting in Queue")

		plt.legend()
		plt.show()

	@staticmethod
	def plot_total_time(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("Customer (n)", fontsize=16, loc="center", color="#ff0033")
		plt.ylabel("Time (s)", fontsize=16, rotation=90, loc="center", color="#ff0033")
		plt.title("Time Spent in System per Customer", fontsize=16, color="#220066")

		plt.ylim(0, max(dd1k.total_time[:70]) + 2)
		plt.xlim(0, 70)

		plt.step(range(len(dd1k.total_time)), dd1k.total_time, color="#336600", linewidth=3, label="Waiting in System")

		plt.legend()
		plt.show()

	@staticmethod
	def plot_arrival_time(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("Customer (n)", fontsize=16, loc="center", color="#ff0033")
		plt.ylabel("Time (s)", fontsize=16, rotation=90, loc="center", color="#ff0033")
		plt.title("Arrival Time per Customer", fontsize=16, color="#220066")

		plt.ylim(0, max(dd1k.customer_arrival_time[:70]) + 2)
		plt.xlim(0, 70)

		plt.step(range(len(dd1k.customer_arrival_time)), dd1k.customer_arrival_time, color="#330033", linewidth=3, label="Arrival Time")

		plt.legend()
		plt.show()

	@staticmethod
	def plot_balking_list(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("Customer (n)", fontsize=16, loc="center", color="#ff0033")
		plt.ylabel("Time (s)", fontsize=16, rotation=90, loc="center", color="#ff0033")
		plt.title("Balking Customers", fontsize=16, color="#220066")

		plt.ylim(0, max(dd1k.balking_customers[:70]) + 2)
		plt.xlim(0, 70)

		plt.stem(range(len(dd1k.balking_customers)), dd1k.balking_customers, label="Balking Entities")

		plt.legend()
		plt.show()
