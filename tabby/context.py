class Context:
    def __init__(self):
        self.num_workers = 1
        self.cpu_arch = "x86_64"
        self.cores_per_worker = 2
        self.accelerator = ["CUDA"]
