import operator_benchmark as op_bench
import torch

"""Microbenchmark for Fill_ operator."""


fill_short_configs = op_bench.cross_product_configs(
    N=[10, 1000],
    device=torch.testing.get_all_device_types(),
    dtype=[torch.ByteTensor, torch.int8, torch.uint8, torch.int16, torch.int32,
           torch.int64, torch.half, torch.float, torch.double],
    tags=["short"]
)


class Fill_Benchmark(op_bench.TorchBenchmarkBase):
    def init(self, N, device, dtype):
        self.input_one = torch.zeros(N, device=device).type(dtype)
        self.set_module_name("fill_")

    def forward(self):
        return self.input_one.fill_(10)


op_bench.generate_pt_test(fill_short_configs, Fill_Benchmark)


if __name__ == "__main__":
    op_bench.benchmark_runner.main()
