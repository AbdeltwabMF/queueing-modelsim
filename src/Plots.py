from matplotlib import pyplot as plt


class Plots:
	@staticmethod
	def plot_system_size_per_time(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("t(s)", fontsize=16, loc="right", color="#ff0033")
		plt.ylabel("n(t)", fontsize=16, rotation=0, loc="top", color="#ff0033")
		plt.title("Customers per Second", fontsize=16, color="#220066")

		plt.ylim(0, dd1k.get_k() + dd1k.get_initial_customers() + 1)
		plt.xlim(0, 70)

		plt.step(range(len(dd1k.system_size_per_time)), dd1k.system_size_per_time, color="#cc0033", linewidth=3)

		plt.show()

	@staticmethod
	def plot_departure(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("Customer", fontsize=16, loc="right", color="#ff0033")
		plt.ylabel("departure time", fontsize=16, rotation=0, loc="top", color="#ff0033")
		plt.title("Departure Time per Customer", fontsize=16, color="#220066")

		plt.ylim(0, dd1k.get_k() + dd1k.get_initial_customers() + 1)
		plt.xlim(0, 70)

		plt.step(range(len(dd1k.departures)), dd1k.departures, color="#00ffcc", linewidth=3)

		plt.show()

	@staticmethod
	def plot_queue_time(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("Customer", fontsize=16, loc="right", color="#ff0033")
		plt.ylabel("queue time", fontsize=16, rotation=0, loc="top", color="#ff0033")
		plt.title("Queue Time per Customer", fontsize=16, color="#220066")

		plt.ylim(0, dd1k.get_k() + dd1k.get_initial_customers() + 1)
		plt.xlim(0, 70)

		plt.step(range(len(dd1k.queue_time)), dd1k.queue_time, color="#0000cc", linewidth=3)

		plt.show()

	@staticmethod
	def plot_total_time(dd1k):

		plt.grid()
		# plt.style.use("fivethirtyeight")

		plt.xlabel("Customer", fontsize=16, loc="right", color="#ff0033")
		plt.ylabel("total time", fontsize=16, rotation=0, loc="top", color="#ff0033")
		plt.title("Total time in the System per Customer", fontsize=16, color="#220066")

		plt.ylim(0, dd1k.get_k() + dd1k.get_initial_customers() + 1)
		plt.xlim(0, 70)

		plt.step(range(len(dd1k.total_time)), dd1k.total_time, color="#3399ff", linewidth=3)

		plt.show()
