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
		plt.xlim(0, 60)

		plt.step(range(len(dd1k.system_size_per_time)), dd1k.system_size_per_time, color="#cc0033", linewidth=3)

		plt.show()

	@staticmethod
	def plot_departure(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("Customer (n)", fontsize=16, loc="center", color="#ff0033")
		plt.ylabel("Time (s)", fontsize=16, rotation=90, loc="center", color="#ff0033")
		plt.title("Departure Time per Customer", fontsize=16, color="#220066")

		plt.ylim(0, max(dd1k.departures[:30]) + 2)
		plt.xlim(0, 30)

		plt.step(range(len(dd1k.departures)), dd1k.departures, color="#cc0033", linewidth=3)

		plt.show()

	@staticmethod
	def plot_queue_time(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("Customer (n)", fontsize=16, loc="center", color="#ff0033")
		plt.ylabel("Time (s)", fontsize=16, rotation=90, loc="center", color="#ff0033")
		plt.title("Time Spent in Queue per Customer", fontsize=16, color="#220066")

		plt.ylim(0, max(dd1k.queue_time[:30]) + 2)
		plt.xlim(0, 30)

		plt.step(range(len(dd1k.queue_time)), dd1k.queue_time, color="#cc0033", linewidth=3)

		plt.show()

	@staticmethod
	def plot_total_time(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("Customer (n)", fontsize=16, loc="center", color="#ff0033")
		plt.ylabel("Time (s)", fontsize=16, rotation=90, loc="center", color="#ff0033")
		plt.title("Time Spent in System per Customer", fontsize=16, color="#220066")

		plt.ylim(0, max(dd1k.total_time[:30]) + 2)
		plt.xlim(0, 30)

		plt.step(range(len(dd1k.total_time)), dd1k.total_time, color="#cc0033", linewidth=3)

		plt.show()
