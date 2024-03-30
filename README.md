# Queueing ModelSim

This software is designed to calculate the characteristics of different queues using the BMAP (Batch Markovian Arrival Process) as input, and deterministic queues characterized by units of input (i.e., customers) arriving at known points in time with fixed service intervals.

## About Queueing Theory

### Definition

Queueing theory is a powerful tool for analyzing the daily phenomenon of waiting in line. Learn how to define queueing theory, its origins, significance, and real-life applications.

Typical examples include:

- Banks/supermarkets: waiting for service
- Computers: waiting for a response
- Public transport: waiting for a train or bus

### Different Types of Queueing Systems

Also known as Kendall's Notation with the format `A/B/C/D/E`, where:

- `A` represents the probability distribution for the arrival process
- `B` represents the probability distribution for the service process
- `C` represents the number of channels (servers)
- `D` represents the maximum number of customers allowed in the queueing system (either being served or waiting for service)
- `E` represents the maximum total number of customers

Common options for `A` and `B` are:

- `M` for a Poisson arrival distribution (exponential inter-arrival distribution) or an exponential service time distribution
- `D` for a deterministic or constant value
- `G` for a general distribution (with known mean and variance)

If `D` and `E` are not specified, it is assumed that they are infinite.

Common symbols used include:

- `λ` for the mean arrival rate
- `µ` for the mean service rate

## What It Does and How to Use It

### Prerequisite Libraries

- Install Python 3: `sudo apt install python3`
- Install pip for Python 3: `sudo apt install python3-pip`
- Install required libraries: `sudo pip3 install tk matplotlib`

1. Clone or download the repository using the following command:
   `git clone https://github.com/AbdeltwabMF/Queueing-ModelSim`
   ![Clone](./screenshots/Clone.png)

2. Navigate to the `Queueing-ModelSim/src` directory and run `python3 main.py`.

   - Choose the queueing model you want to calculate: `D/D/1/K`, `M/M/1`, `M/M/1/K`, `M/M/C`, or `M/M/C/K`.
   - Input the arrival rate (`λ`) and service rates (`µ`).
   - Provide additional parameters such as the number of servers (`C`) and maximum number of entities (`K` or `M`).
   - Press "Calculate".

   ![Run](./screenshots/Run.png)

3. For Deterministic Queues (`D/D/1/K`), a window will prompt you to choose the data you want to plot.
   ![Deterministic](./screenshots/Deterministic.png)

## Plots

The following figures depict various aspects of the queueing system:

- Number of entities (customers) in the system at each unit of time.
   ![Entities_in_System](./screenshots/Entities_in_System.png)
- Time that customer n spends in the queue to be served.
   ![Waiting_in_queue](./screenshots/Waiting_in_queue.png)
- Time that customer n spends in the system until departure.
   ![Waiting_in_System](./screenshots/Waiting_in_System.png)
- Time of departure for each entity (customer).
   ![Departure_time](./screenshots/Departure_time.png)
- Customers who balked and corresponding processing time.
   ![Balking_customers](./screenshots/Balking_customers.png)
- Arrival time of each entity.
   ![Arrival_time](./screenshots/Arrival_time.png)

For Stochastic Models, a window will display server utilization (`rho`), average entities in the system (`L`), average entities in queue (`Lq`), average time an entity spends in the system (`W`), and average time an entity waits in line to be served (`Wq`).
![Stochastic](./screenshots/Stochastic.png)

## License

Licensed under the [GPL-3.0 License](LICENSE.md)
