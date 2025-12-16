import sys

class JobError(Exception):
    pass


# Job Class 
class Job:
    MAX_CPU = 128
    MAX_MEM = 512
    MAX_RUNTIME = 86400

    def __init__(self, cpu, memory, runtime):
        if cpu < 0 or memory < 0 or runtime < 0:
            raise JobError("Negative resource values are not allowed")

        self.cpu = cpu
        self.memory = memory
        self.runtime = runtime

    # Overload + operator
    def __add__(self, other):
        try:
            new_cpu = self.cpu + other.cpu
            new_mem = self.memory + other.memory
            new_runtime = self.runtime + other.runtime

            if (new_cpu > Job.MAX_CPU or
                new_mem > Job.MAX_MEM or
                new_runtime > Job.MAX_RUNTIME):
                raise JobError("Resource overflow during job merge")

            return Job(new_cpu, new_mem, new_runtime)

        except JobError as e:
            raise e

    # Weighted cost calculation (no object modification)
    def cost(self):
        return (self.cpu * 3) + (self.memory * 2) + (self.runtime * 0.01)

    # Overload > operator
    def __gt__(self, other):
        return self.cost() > other.cost()

    def __str__(self):
        return f"CPU={self.cpu}, MEM={self.memory}, RT={self.runtime}"


def write_job(queue_file, job):
    with open(queue_file, "a") as f:
        f.write(str(job) + "\n")


def log_failure(log_file, message):
    with open(log_file, "a") as f:
        f.write(message + "\n")


def main():
    job_queue = "job_queue.txt"
    failure_log = "failure_log.txt"

    # Dummy jobs
    job1 = Job(16, 32, 3000)
    job2 = Job(8, 16, 2000)
    job3 = Job(120, 500, 80000)  # risky job

    write_job(job_queue, job1)
    write_job(job_queue, job2)

    print("Initial jobs added to queue.")

    # Exception-safe job merging
    try:
        merged_job = job1 + job2
        write_job(job_queue, merged_job)
        print("Merged Job:", merged_job)

    except JobError as e:
        log_failure(failure_log, str(e))
        print("Merge failed:", e)

    # Overflow example
    try:
        bad_merge = job1 + job3
        write_job(job_queue, bad_merge)

    except JobError as e:
        log_failure(failure_log, str(e))
        print("Overflow detected:", e)

    # Priority evaluation
    print("\nPriority Check:")
    if job1 > job2:
        print("Job1 has higher priority than Job2")
    else:
        print("Job2 has higher priority than Job1")


if __name__ == "__main__":
    main()

