from collections import namedtuple


Disk = namedtuple('Disk', 'major_number minor_number device_name read_count read_merged_count read_sections time_spent_reading write_count write_merged_count write_sections time_spent_write io_requests time_spent_doing_io weighted_time_spent_doing_io')

b = ' 11       0 sr0 18 0 2056 49 0 0 0 0 0 42 49'
print(b.split())
a = Disk(*(b.split()))