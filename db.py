from config import *
from datetime import datetime
from sqlalchemy import MetaData, Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()


class Virtualmachine(Base):
    __tablename__ = 'xiaoice_virtualmachine'
    id = Column(Integer, primary_key=True)
    key = Column(String(255))
    display = Column(String(255))
    location_id = Column(Integer)
    provider_id = Column(Integer)


class Provider(Base):
    __tablename__ = 'xiaoice_provider'
    id = Column(Integer, primary_key=True)
    key = Column(String(255))
    display = Column(String(255))


class Location(Base):
    __tablename__ = 'xiaoice_location'
    id = Column(Integer, primary_key=True)
    key = Column(String(255))
    display = Column(String(255))


class Operatingsystem(Base):
    __tablename__ = 'xiaoice_operatingsystem'
    id = Column(Integer, primary_key=True)
    key = Column(String(255))
    display = Column(String(255))


class Cores(Base):
    __tablename__ = 'xiaoice_cores'
    id = Column(Integer, primary_key=True)
    key = Column(String(255))
    number = Column(String(255))


class Disksizes(Base):
    __tablename__ = 'xiaoice_disksizes'
    id = Column(Integer, primary_key=True)
    key = Column(String(255))
    size = Column(String(255))


class Processordata(Base):
    __tablename__ = 'xiaoice_processordata'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    vm_id = Column(Integer, nullable=False)
    os_id = Column(Integer, nullable=True)
    performance = Column(Integer, nullable=True)
    processor = Column(String(100), nullable=True)
    runtime = Column(Float(30), nullable=True)
    intmulti = Column(Integer, nullable=True)
    floatmulti = Column(Integer, nullable=True)
    totalmulti = Column(Integer, nullable=True)
    intsingle = Column(Integer, nullable=True)
    floatsingle = Column(Integer, nullable=True)
    totalsingle = Column(Integer, nullable=True)
    aes = Column(Float(30), nullable=True)
    twofish = Column(Float(30), nullable=True)
    sha1 = Column(Float(30), nullable=True)
    sha2 = Column(Float(30), nullable=True)
    bzipcompression = Column(Float(30), nullable=True)
    bzipdecompression = Column(Float(30), nullable=True)
    jpegcompression = Column(Float(30), nullable=True)
    jpegdecompression = Column(Float(30), nullable=True)
    pngcompression = Column(Float(30), nullable=True)
    pngdecompression = Column(Float(30), nullable=True)
    sobel = Column(Float(30), nullable=True)
    lua = Column(Float(30), nullable=True)
    dijkstra = Column(Float(30), nullable=True)
    blackscholes = Column(Float(30), nullable=True)
    mandelbrot = Column(Float(30), nullable=True)
    sharpenimage = Column(Float(30), nullable=True)
    blurimage = Column(Float(30), nullable=True)
    sgemm = Column(Float(30), nullable=True)
    dgemm = Column(Float(30), nullable=True)
    sfft = Column(Float(30), nullable=True)
    dfft = Column(Float(30), nullable=True)
    nbody = Column(Float(30), nullable=True)
    raytrace = Column(Float(30), nullable=True)


class Memorydata(Base):
    __tablename__ = 'xiaoice_memorydata'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    vm_id = Column(Integer, nullable=False)
    os_id = Column(Integer, nullable=True)
    bandwidth = Column(Float(30), nullable=True)
    copy = Column(Float(30), nullable=True)
    scale = Column(Float(30), nullable=True)
    add = Column(Float(30), nullable=True)
    triad = Column(Float(30), nullable=True)
    memsingle = Column(Integer, nullable=True)
    memmulti = Column(Integer, nullable=True)


class Localdiskdata(Base):
    __tablename__ = 'xiaoice_localdiskdata'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    vm_id = Column(Integer, nullable=False)
    os_id = Column(Integer, nullable=True)
    iops_write_100_seq = Column(Float(30), nullable=True)
    throughput_write_100_seq = Column(Float(30), nullable=True)
    lat_write_100_seq = Column(Float(30), nullable=True)
    iops_read_100_seq = Column(Float(30), nullable=True)
    throughput_read_100_seq = Column(Float(30), nullable=True)
    lat_read_100_seq = Column(Float(30), nullable=True)
    iops_write_100_random = Column(Float(30), nullable=True)
    throughput_write_100_random = Column(Float(30), nullable=True)
    lat_write_100_random = Column(Float(30), nullable=True)
    iops_read_100_random = Column(Float(30), nullable=True)
    throughput_read_100_random = Column(Float(30), nullable=True)
    lat_read_100_random = Column(Float(30), nullable=True)
    iops_read_seq = Column(Float(30), nullable=True)
    iops_write_seq = Column(Float(30), nullable=True)
    iops_read_random = Column(Float(30), nullable=True)
    iops_write_random = Column(Float(30), nullable=True)
    throughput_read_seq = Column(Float(30), nullable=True)
    throughput_write_seq = Column(Float(30), nullable=True)
    throughput_read_random = Column(Float(30), nullable=True)
    throughput_write_random = Column(Float(30), nullable=True)
    latency_read_seq = Column(Float(30), nullable=True)
    latency_write_seq = Column(Float(30), nullable=True)
    latency_read_random = Column(Float(30), nullable=True)
    latency_write_random = Column(Float(30), nullable=True)


class Blockdiskdata(Base):
    __tablename__ = 'xiaoice_blockdiskdata'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    vm_id = Column(Integer, nullable=False)
    disk_size_id = Column(Integer, nullable=True)
    os_id = Column(Integer, nullable=True)
    iops_write_100_seq = Column(Float(30), nullable=True)
    throughput_write_100_seq = Column(Float(30), nullable=True)
    lat_write_100_seq = Column(Float(30), nullable=True)
    iops_read_100_seq = Column(Float(30), nullable=True)
    throughput_read_100_seq = Column(Float(30), nullable=True)
    lat_read_100_seq = Column(Float(30), nullable=True)
    iops_write_100_random = Column(Float(30), nullable=True)
    throughput_write_100_random = Column(Float(30), nullable=True)
    lat_write_100_random = Column(Float(30), nullable=True)
    iops_read_100_random = Column(Float(30), nullable=True)
    throughput_read_100_random = Column(Float(30), nullable=True)
    lat_read_100_random = Column(Float(30), nullable=True)
    iops_read_seq = Column(Float(30), nullable=True)
    iops_write_seq = Column(Float(30), nullable=True)
    iops_read_random = Column(Float(30), nullable=True)
    iops_write_random = Column(Float(30), nullable=True)
    throughput_read_seq = Column(Float(30), nullable=True)
    throughput_write_seq = Column(Float(30), nullable=True)
    throughput_read_random = Column(Float(30), nullable=True)
    throughput_write_random = Column(Float(30), nullable=True)
    latency_read_seq = Column(Float(30), nullable=True)
    latency_write_seq = Column(Float(30), nullable=True)
    latency_read_random = Column(Float(30), nullable=True)
    latency_write_random = Column(Float(30), nullable=True)


class Internalnetworkdata(Base):
    __tablename__ = 'xiaoice_internalnetworkdata'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    vm_id = Column(Integer, nullable=False)
    os_id = Column(Integer, nullable=True)
    single_threaded_throughput = Column(Float(30), nullable=True)
    multi_threaded_throughput = Column(Float(30), nullable=True)


class Processoraggdata(Base):
    __tablename__ = 'xiaoice_processoraggdata'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    vm_id = Column(Integer, nullable=False)
    os_id = Column(Integer, nullable=False)
    month_min = Column(Float(30), nullable=True)
    month_25 = Column(Float(30), nullable=True)
    month_75 = Column(Float(30), nullable=True)
    month_max = Column(Float(30), nullable=True)
    month_median = Column(Float(30), nullable=True)
    year_min = Column(Float(30), nullable=True)
    year_25 = Column(Float(30), nullable=True)
    year_75 = Column(Float(30), nullable=True)
    year_max = Column(Float(30), nullable=True)
    year_median = Column(Float(30), nullable=True)
    lifetime_min = Column(Float(30), nullable=True)
    lifetime_25 = Column(Float(30), nullable=True)
    lifetime_75 = Column(Float(30), nullable=True)
    lifetime_max = Column(Float(30), nullable=True)
    lifetime_median = Column(Float(30), nullable=True)


class Memoryaggdata(Base):
    __tablename__ = 'xiaoice_memoryaggdata'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    vm_id = Column(Integer, nullable=False)
    os_id = Column(Integer, nullable=False)
    month_min = Column(Float(30), nullable=True)
    month_25 = Column(Float(30), nullable=True)
    month_75 = Column(Float(30), nullable=True)
    month_max = Column(Float(30), nullable=True)
    month_median = Column(Float(30), nullable=True)
    year_min = Column(Float(30), nullable=True)
    year_25 = Column(Float(30), nullable=True)
    year_75 = Column(Float(30), nullable=True)
    year_max = Column(Float(30), nullable=True)
    year_median = Column(Float(30), nullable=True)
    lifetime_min = Column(Float(30), nullable=True)
    lifetime_25 = Column(Float(30), nullable=True)
    lifetime_75 = Column(Float(30), nullable=True)
    lifetime_max = Column(Float(30), nullable=True)
    lifetime_median = Column(Float(30), nullable=True)


class Localdiskaggdata(Base):
    __tablename__ = 'xiaoice_localdiskaggdata'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    vm_id = Column(Integer, nullable=False)
    os_id = Column(Integer, nullable=False)
    iops_read_seq_month_min = Column(Float(30), nullable=True)
    iops_read_seq_month_25 = Column(Float(30), nullable=True)
    iops_read_seq_month_75 = Column(Float(30), nullable=True)
    iops_read_seq_month_max = Column(Float(30), nullable=True)
    iops_read_seq_month_median = Column(Float(30), nullable=True)
    iops_read_seq_year_min = Column(Float(30), nullable=True)
    iops_read_seq_year_25 = Column(Float(30), nullable=True)
    iops_read_seq_year_75 = Column(Float(30), nullable=True)
    iops_read_seq_year_max = Column(Float(30), nullable=True)
    iops_read_seq_year_median = Column(Float(30), nullable=True)
    iops_read_seq_lifetime_min = Column(Float(30), nullable=True)
    iops_read_seq_lifetime_25 = Column(Float(30), nullable=True)
    iops_read_seq_lifetime_75 = Column(Float(30), nullable=True)
    iops_read_seq_lifetime_max = Column(Float(30), nullable=True)
    iops_read_seq_lifetime_median = Column(Float(30), nullable=True)
    iops_write_seq_month_min = Column(Float(30), nullable=True)
    iops_write_seq_month_25 = Column(Float(30), nullable=True)
    iops_write_seq_month_75 = Column(Float(30), nullable=True)
    iops_write_seq_month_max = Column(Float(30), nullable=True)
    iops_write_seq_month_median = Column(Float(30), nullable=True)
    iops_write_seq_year_min = Column(Float(30), nullable=True)
    iops_write_seq_year_25 = Column(Float(30), nullable=True)
    iops_write_seq_year_75 = Column(Float(30), nullable=True)
    iops_write_seq_year_max = Column(Float(30), nullable=True)
    iops_write_seq_year_median = Column(Float(30), nullable=True)
    iops_write_seq_lifetime_min = Column(Float(30), nullable=True)
    iops_write_seq_lifetime_25 = Column(Float(30), nullable=True)
    iops_write_seq_lifetime_75 = Column(Float(30), nullable=True)
    iops_write_seq_lifetime_max = Column(Float(30), nullable=True)
    iops_write_seq_lifetime_median = Column(Float(30), nullable=True)
    iops_read_random_month_min = Column(Float(30), nullable=True)
    iops_read_random_month_25 = Column(Float(30), nullable=True)
    iops_read_random_month_75 = Column(Float(30), nullable=True)
    iops_read_random_month_max = Column(Float(30), nullable=True)
    iops_read_random_month_median = Column(Float(30), nullable=True)
    iops_read_random_year_min = Column(Float(30), nullable=True)
    iops_read_random_year_25 = Column(Float(30), nullable=True)
    iops_read_random_year_75 = Column(Float(30), nullable=True)
    iops_read_random_year_max = Column(Float(30), nullable=True)
    iops_read_random_year_median = Column(Float(30), nullable=True)
    iops_read_random_lifetime_min = Column(Float(30), nullable=True)
    iops_read_random_lifetime_25 = Column(Float(30), nullable=True)
    iops_read_random_lifetime_75 = Column(Float(30), nullable=True)
    iops_read_random_lifetime_max = Column(Float(30), nullable=True)
    iops_read_random_lifetime_median = Column(Float(30), nullable=True)
    iops_write_random_month_min = Column(Float(30), nullable=True)
    iops_write_random_month_25 = Column(Float(30), nullable=True)
    iops_write_random_month_75 = Column(Float(30), nullable=True)
    iops_write_random_month_max = Column(Float(30), nullable=True)
    iops_write_random_month_median = Column(Float(30), nullable=True)
    iops_write_random_year_min = Column(Float(30), nullable=True)
    iops_write_random_year_25 = Column(Float(30), nullable=True)
    iops_write_random_year_75 = Column(Float(30), nullable=True)
    iops_write_random_year_max = Column(Float(30), nullable=True)
    iops_write_random_year_median = Column(Float(30), nullable=True)
    iops_write_random_lifetime_min = Column(Float(30), nullable=True)
    iops_write_random_lifetime_25 = Column(Float(30), nullable=True)
    iops_write_random_lifetime_75 = Column(Float(30), nullable=True)
    iops_write_random_lifetime_max = Column(Float(30), nullable=True)
    iops_write_random_lifetime_median = Column(Float(30), nullable=True)
    throughput_read_seq_month_min = Column(Float(30), nullable=True)
    throughput_read_seq_month_25 = Column(Float(30), nullable=True)
    throughput_read_seq_month_75 = Column(Float(30), nullable=True)
    throughput_read_seq_month_max = Column(Float(30), nullable=True)
    throughput_read_seq_month_median = Column(Float(30), nullable=True)
    throughput_read_seq_year_min = Column(Float(30), nullable=True)
    throughput_read_seq_year_25 = Column(Float(30), nullable=True)
    throughput_read_seq_year_75 = Column(Float(30), nullable=True)
    throughput_read_seq_year_max = Column(Float(30), nullable=True)
    throughput_read_seq_year_median = Column(Float(30), nullable=True)
    throughput_read_seq_lifetime_min = Column(Float(30), nullable=True)
    throughput_read_seq_lifetime_25 = Column(Float(30), nullable=True)
    throughput_read_seq_lifetime_75 = Column(Float(30), nullable=True)
    throughput_read_seq_lifetime_max = Column(Float(30), nullable=True)
    throughput_read_seq_lifetime_median = Column(Float(30), nullable=True)
    throughput_write_seq_month_min = Column(Float(30), nullable=True)
    throughput_write_seq_month_25 = Column(Float(30), nullable=True)
    throughput_write_seq_month_75 = Column(Float(30), nullable=True)
    throughput_write_seq_month_max = Column(Float(30), nullable=True)
    throughput_write_seq_month_median = Column(Float(30), nullable=True)
    throughput_write_seq_year_min = Column(Float(30), nullable=True)
    throughput_write_seq_year_25 = Column(Float(30), nullable=True)
    throughput_write_seq_year_75 = Column(Float(30), nullable=True)
    throughput_write_seq_year_max = Column(Float(30), nullable=True)
    throughput_write_seq_year_median = Column(Float(30), nullable=True)
    throughput_write_seq_lifetime_min = Column(Float(30), nullable=True)
    throughput_write_seq_lifetime_25 = Column(Float(30), nullable=True)
    throughput_write_seq_lifetime_75 = Column(Float(30), nullable=True)
    throughput_write_seq_lifetime_max = Column(Float(30), nullable=True)
    throughput_write_seq_lifetime_median = Column(Float(30), nullable=True)
    throughput_read_random_month_min = Column(Float(30), nullable=True)
    throughput_read_random_month_25 = Column(Float(30), nullable=True)
    throughput_read_random_month_75 = Column(Float(30), nullable=True)
    throughput_read_random_month_max = Column(Float(30), nullable=True)
    throughput_read_random_month_median = Column(Float(30), nullable=True)
    throughput_read_random_year_min = Column(Float(30), nullable=True)
    throughput_read_random_year_25 = Column(Float(30), nullable=True)
    throughput_read_random_year_75 = Column(Float(30), nullable=True)
    throughput_read_random_year_max = Column(Float(30), nullable=True)
    throughput_read_random_year_median = Column(Float(30), nullable=True)
    throughput_read_random_lifetime_min = Column(Float(30), nullable=True)
    throughput_read_random_lifetime_25 = Column(Float(30), nullable=True)
    throughput_read_random_lifetime_75 = Column(Float(30), nullable=True)
    throughput_read_random_lifetime_max = Column(Float(30), nullable=True)
    throughput_read_random_lifetime_median = Column(Float(30), nullable=True)
    throughput_write_random_month_min = Column(Float(30), nullable=True)
    throughput_write_random_month_25 = Column(Float(30), nullable=True)
    throughput_write_random_month_75 = Column(Float(30), nullable=True)
    throughput_write_random_month_max = Column(Float(30), nullable=True)
    throughput_write_random_month_median = Column(Float(30), nullable=True)
    throughput_write_random_year_min = Column(Float(30), nullable=True)
    throughput_write_random_year_25 = Column(Float(30), nullable=True)
    throughput_write_random_year_75 = Column(Float(30), nullable=True)
    throughput_write_random_year_max = Column(Float(30), nullable=True)
    throughput_write_random_year_median = Column(Float(30), nullable=True)
    throughput_write_random_lifetime_min = Column(Float(30), nullable=True)
    throughput_write_random_lifetime_25 = Column(Float(30), nullable=True)
    throughput_write_random_lifetime_75 = Column(Float(30), nullable=True)
    throughput_write_random_lifetime_max = Column(Float(30), nullable=True)
    throughput_write_random_lifetime_median = Column(Float(30), nullable=True)
    latency_read_seq_month_min = Column(Float(30), nullable=True)
    latency_read_seq_month_25 = Column(Float(30), nullable=True)
    latency_read_seq_month_75 = Column(Float(30), nullable=True)
    latency_read_seq_month_max = Column(Float(30), nullable=True)
    latency_read_seq_month_median = Column(Float(30), nullable=True)
    latency_read_seq_year_min = Column(Float(30), nullable=True)
    latency_read_seq_year_25 = Column(Float(30), nullable=True)
    latency_read_seq_year_75 = Column(Float(30), nullable=True)
    latency_read_seq_year_max = Column(Float(30), nullable=True)
    latency_read_seq_year_median = Column(Float(30), nullable=True)
    latency_read_seq_lifetime_min = Column(Float(30), nullable=True)
    latency_read_seq_lifetime_25 = Column(Float(30), nullable=True)
    latency_read_seq_lifetime_75 = Column(Float(30), nullable=True)
    latency_read_seq_lifetime_max = Column(Float(30), nullable=True)
    latency_read_seq_lifetime_median = Column(Float(30), nullable=True)
    latency_write_seq_month_min = Column(Float(30), nullable=True)
    latency_write_seq_month_25 = Column(Float(30), nullable=True)
    latency_write_seq_month_75 = Column(Float(30), nullable=True)
    latency_write_seq_month_max = Column(Float(30), nullable=True)
    latency_write_seq_month_median = Column(Float(30), nullable=True)
    latency_write_seq_year_min = Column(Float(30), nullable=True)
    latency_write_seq_year_25 = Column(Float(30), nullable=True)
    latency_write_seq_year_75 = Column(Float(30), nullable=True)
    latency_write_seq_year_max = Column(Float(30), nullable=True)
    latency_write_seq_year_median = Column(Float(30), nullable=True)
    latency_write_seq_lifetime_min = Column(Float(30), nullable=True)
    latency_write_seq_lifetime_25 = Column(Float(30), nullable=True)
    latency_write_seq_lifetime_75 = Column(Float(30), nullable=True)
    latency_write_seq_lifetime_max = Column(Float(30), nullable=True)
    latency_write_seq_lifetime_median = Column(Float(30), nullable=True)
    latency_read_random_month_min = Column(Float(30), nullable=True)
    latency_read_random_month_25 = Column(Float(30), nullable=True)
    latency_read_random_month_75 = Column(Float(30), nullable=True)
    latency_read_random_month_max = Column(Float(30), nullable=True)
    latency_read_random_month_median = Column(Float(30), nullable=True)
    latency_read_random_year_min = Column(Float(30), nullable=True)
    latency_read_random_year_25 = Column(Float(30), nullable=True)
    latency_read_random_year_75 = Column(Float(30), nullable=True)
    latency_read_random_year_max = Column(Float(30), nullable=True)
    latency_read_random_year_median = Column(Float(30), nullable=True)
    latency_read_random_lifetime_min = Column(Float(30), nullable=True)
    latency_read_random_lifetime_25 = Column(Float(30), nullable=True)
    latency_read_random_lifetime_75 = Column(Float(30), nullable=True)
    latency_read_random_lifetime_max = Column(Float(30), nullable=True)
    latency_read_random_lifetime_median = Column(Float(30), nullable=True)
    latency_write_random_month_min = Column(Float(30), nullable=True)
    latency_write_random_month_25 = Column(Float(30), nullable=True)
    latency_write_random_month_75 = Column(Float(30), nullable=True)
    latency_write_random_month_max = Column(Float(30), nullable=True)
    latency_write_random_month_median = Column(Float(30), nullable=True)
    latency_write_random_year_min = Column(Float(30), nullable=True)
    latency_write_random_year_25 = Column(Float(30), nullable=True)
    latency_write_random_year_75 = Column(Float(30), nullable=True)
    latency_write_random_year_max = Column(Float(30), nullable=True)
    latency_write_random_year_median = Column(Float(30), nullable=True)
    latency_write_random_lifetime_min = Column(Float(30), nullable=True)
    latency_write_random_lifetime_25 = Column(Float(30), nullable=True)
    latency_write_random_lifetime_75 = Column(Float(30), nullable=True)
    latency_write_random_lifetime_max = Column(Float(30), nullable=True)
    latency_write_random_lifetime_median = Column(Float(30), nullable=True)


class Blockdiskaggdata(Base):
    __tablename__ = 'xiaoice_blockdiskaggdata'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    vm_id = Column(Integer, nullable=False)
    disk_size_id = Column(Integer, nullable=False)
    os_id = Column(Integer, nullable=False)
    iops_read_seq_month_min = Column(Float(30), nullable=True)
    iops_read_seq_month_25 = Column(Float(30), nullable=True)
    iops_read_seq_month_75 = Column(Float(30), nullable=True)
    iops_read_seq_month_max = Column(Float(30), nullable=True)
    iops_read_seq_month_median = Column(Float(30), nullable=True)
    iops_read_seq_year_min = Column(Float(30), nullable=True)
    iops_read_seq_year_25 = Column(Float(30), nullable=True)
    iops_read_seq_year_75 = Column(Float(30), nullable=True)
    iops_read_seq_year_max = Column(Float(30), nullable=True)
    iops_read_seq_year_median = Column(Float(30), nullable=True)
    iops_read_seq_lifetime_min = Column(Float(30), nullable=True)
    iops_read_seq_lifetime_25 = Column(Float(30), nullable=True)
    iops_read_seq_lifetime_75 = Column(Float(30), nullable=True)
    iops_read_seq_lifetime_max = Column(Float(30), nullable=True)
    iops_read_seq_lifetime_median = Column(Float(30), nullable=True)
    iops_write_seq_month_min = Column(Float(30), nullable=True)
    iops_write_seq_month_25 = Column(Float(30), nullable=True)
    iops_write_seq_month_75 = Column(Float(30), nullable=True)
    iops_write_seq_month_max = Column(Float(30), nullable=True)
    iops_write_seq_month_median = Column(Float(30), nullable=True)
    iops_write_seq_year_min = Column(Float(30), nullable=True)
    iops_write_seq_year_25 = Column(Float(30), nullable=True)
    iops_write_seq_year_75 = Column(Float(30), nullable=True)
    iops_write_seq_year_max = Column(Float(30), nullable=True)
    iops_write_seq_year_median = Column(Float(30), nullable=True)
    iops_write_seq_lifetime_min = Column(Float(30), nullable=True)
    iops_write_seq_lifetime_25 = Column(Float(30), nullable=True)
    iops_write_seq_lifetime_75 = Column(Float(30), nullable=True)
    iops_write_seq_lifetime_max = Column(Float(30), nullable=True)
    iops_write_seq_lifetime_median = Column(Float(30), nullable=True)
    iops_read_random_month_min = Column(Float(30), nullable=True)
    iops_read_random_month_25 = Column(Float(30), nullable=True)
    iops_read_random_month_75 = Column(Float(30), nullable=True)
    iops_read_random_month_max = Column(Float(30), nullable=True)
    iops_read_random_month_median = Column(Float(30), nullable=True)
    iops_read_random_year_min = Column(Float(30), nullable=True)
    iops_read_random_year_25 = Column(Float(30), nullable=True)
    iops_read_random_year_75 = Column(Float(30), nullable=True)
    iops_read_random_year_max = Column(Float(30), nullable=True)
    iops_read_random_year_median = Column(Float(30), nullable=True)
    iops_read_random_lifetime_min = Column(Float(30), nullable=True)
    iops_read_random_lifetime_25 = Column(Float(30), nullable=True)
    iops_read_random_lifetime_75 = Column(Float(30), nullable=True)
    iops_read_random_lifetime_max = Column(Float(30), nullable=True)
    iops_read_random_lifetime_median = Column(Float(30), nullable=True)
    iops_write_random_month_min = Column(Float(30), nullable=True)
    iops_write_random_month_25 = Column(Float(30), nullable=True)
    iops_write_random_month_75 = Column(Float(30), nullable=True)
    iops_write_random_month_max = Column(Float(30), nullable=True)
    iops_write_random_month_median = Column(Float(30), nullable=True)
    iops_write_random_year_min = Column(Float(30), nullable=True)
    iops_write_random_year_25 = Column(Float(30), nullable=True)
    iops_write_random_year_75 = Column(Float(30), nullable=True)
    iops_write_random_year_max = Column(Float(30), nullable=True)
    iops_write_random_year_median = Column(Float(30), nullable=True)
    iops_write_random_lifetime_min = Column(Float(30), nullable=True)
    iops_write_random_lifetime_25 = Column(Float(30), nullable=True)
    iops_write_random_lifetime_75 = Column(Float(30), nullable=True)
    iops_write_random_lifetime_max = Column(Float(30), nullable=True)
    iops_write_random_lifetime_median = Column(Float(30), nullable=True)
    throughput_read_seq_month_min = Column(Float(30), nullable=True)
    throughput_read_seq_month_25 = Column(Float(30), nullable=True)
    throughput_read_seq_month_75 = Column(Float(30), nullable=True)
    throughput_read_seq_month_max = Column(Float(30), nullable=True)
    throughput_read_seq_month_median = Column(Float(30), nullable=True)
    throughput_read_seq_year_min = Column(Float(30), nullable=True)
    throughput_read_seq_year_25 = Column(Float(30), nullable=True)
    throughput_read_seq_year_75 = Column(Float(30), nullable=True)
    throughput_read_seq_year_max = Column(Float(30), nullable=True)
    throughput_read_seq_year_median = Column(Float(30), nullable=True)
    throughput_read_seq_lifetime_min = Column(Float(30), nullable=True)
    throughput_read_seq_lifetime_25 = Column(Float(30), nullable=True)
    throughput_read_seq_lifetime_75 = Column(Float(30), nullable=True)
    throughput_read_seq_lifetime_max = Column(Float(30), nullable=True)
    throughput_read_seq_lifetime_median = Column(Float(30), nullable=True)
    throughput_write_seq_month_min = Column(Float(30), nullable=True)
    throughput_write_seq_month_25 = Column(Float(30), nullable=True)
    throughput_write_seq_month_75 = Column(Float(30), nullable=True)
    throughput_write_seq_month_max = Column(Float(30), nullable=True)
    throughput_write_seq_month_median = Column(Float(30), nullable=True)
    throughput_write_seq_year_min = Column(Float(30), nullable=True)
    throughput_write_seq_year_25 = Column(Float(30), nullable=True)
    throughput_write_seq_year_75 = Column(Float(30), nullable=True)
    throughput_write_seq_year_max = Column(Float(30), nullable=True)
    throughput_write_seq_year_median = Column(Float(30), nullable=True)
    throughput_write_seq_lifetime_min = Column(Float(30), nullable=True)
    throughput_write_seq_lifetime_25 = Column(Float(30), nullable=True)
    throughput_write_seq_lifetime_75 = Column(Float(30), nullable=True)
    throughput_write_seq_lifetime_max = Column(Float(30), nullable=True)
    throughput_write_seq_lifetime_median = Column(Float(30), nullable=True)
    throughput_read_random_month_min = Column(Float(30), nullable=True)
    throughput_read_random_month_25 = Column(Float(30), nullable=True)
    throughput_read_random_month_75 = Column(Float(30), nullable=True)
    throughput_read_random_month_max = Column(Float(30), nullable=True)
    throughput_read_random_month_median = Column(Float(30), nullable=True)
    throughput_read_random_year_min = Column(Float(30), nullable=True)
    throughput_read_random_year_25 = Column(Float(30), nullable=True)
    throughput_read_random_year_75 = Column(Float(30), nullable=True)
    throughput_read_random_year_max = Column(Float(30), nullable=True)
    throughput_read_random_year_median = Column(Float(30), nullable=True)
    throughput_read_random_lifetime_min = Column(Float(30), nullable=True)
    throughput_read_random_lifetime_25 = Column(Float(30), nullable=True)
    throughput_read_random_lifetime_75 = Column(Float(30), nullable=True)
    throughput_read_random_lifetime_max = Column(Float(30), nullable=True)
    throughput_read_random_lifetime_median = Column(Float(30), nullable=True)
    throughput_write_random_month_min = Column(Float(30), nullable=True)
    throughput_write_random_month_25 = Column(Float(30), nullable=True)
    throughput_write_random_month_75 = Column(Float(30), nullable=True)
    throughput_write_random_month_max = Column(Float(30), nullable=True)
    throughput_write_random_month_median = Column(Float(30), nullable=True)
    throughput_write_random_year_min = Column(Float(30), nullable=True)
    throughput_write_random_year_25 = Column(Float(30), nullable=True)
    throughput_write_random_year_75 = Column(Float(30), nullable=True)
    throughput_write_random_year_max = Column(Float(30), nullable=True)
    throughput_write_random_year_median = Column(Float(30), nullable=True)
    throughput_write_random_lifetime_min = Column(Float(30), nullable=True)
    throughput_write_random_lifetime_25 = Column(Float(30), nullable=True)
    throughput_write_random_lifetime_75 = Column(Float(30), nullable=True)
    throughput_write_random_lifetime_max = Column(Float(30), nullable=True)
    throughput_write_random_lifetime_median = Column(Float(30), nullable=True)
    latency_read_seq_month_min = Column(Float(30), nullable=True)
    latency_read_seq_month_25 = Column(Float(30), nullable=True)
    latency_read_seq_month_75 = Column(Float(30), nullable=True)
    latency_read_seq_month_max = Column(Float(30), nullable=True)
    latency_read_seq_month_median = Column(Float(30), nullable=True)
    latency_read_seq_year_min = Column(Float(30), nullable=True)
    latency_read_seq_year_25 = Column(Float(30), nullable=True)
    latency_read_seq_year_75 = Column(Float(30), nullable=True)
    latency_read_seq_year_max = Column(Float(30), nullable=True)
    latency_read_seq_year_median = Column(Float(30), nullable=True)
    latency_read_seq_lifetime_min = Column(Float(30), nullable=True)
    latency_read_seq_lifetime_25 = Column(Float(30), nullable=True)
    latency_read_seq_lifetime_75 = Column(Float(30), nullable=True)
    latency_read_seq_lifetime_max = Column(Float(30), nullable=True)
    latency_read_seq_lifetime_median = Column(Float(30), nullable=True)
    latency_write_seq_month_min = Column(Float(30), nullable=True)
    latency_write_seq_month_25 = Column(Float(30), nullable=True)
    latency_write_seq_month_75 = Column(Float(30), nullable=True)
    latency_write_seq_month_max = Column(Float(30), nullable=True)
    latency_write_seq_month_median = Column(Float(30), nullable=True)
    latency_write_seq_year_min = Column(Float(30), nullable=True)
    latency_write_seq_year_25 = Column(Float(30), nullable=True)
    latency_write_seq_year_75 = Column(Float(30), nullable=True)
    latency_write_seq_year_max = Column(Float(30), nullable=True)
    latency_write_seq_year_median = Column(Float(30), nullable=True)
    latency_write_seq_lifetime_min = Column(Float(30), nullable=True)
    latency_write_seq_lifetime_25 = Column(Float(30), nullable=True)
    latency_write_seq_lifetime_75 = Column(Float(30), nullable=True)
    latency_write_seq_lifetime_max = Column(Float(30), nullable=True)
    latency_write_seq_lifetime_median = Column(Float(30), nullable=True)
    latency_read_random_month_min = Column(Float(30), nullable=True)
    latency_read_random_month_25 = Column(Float(30), nullable=True)
    latency_read_random_month_75 = Column(Float(30), nullable=True)
    latency_read_random_month_max = Column(Float(30), nullable=True)
    latency_read_random_month_median = Column(Float(30), nullable=True)
    latency_read_random_year_min = Column(Float(30), nullable=True)
    latency_read_random_year_25 = Column(Float(30), nullable=True)
    latency_read_random_year_75 = Column(Float(30), nullable=True)
    latency_read_random_year_max = Column(Float(30), nullable=True)
    latency_read_random_year_median = Column(Float(30), nullable=True)
    latency_read_random_lifetime_min = Column(Float(30), nullable=True)
    latency_read_random_lifetime_25 = Column(Float(30), nullable=True)
    latency_read_random_lifetime_75 = Column(Float(30), nullable=True)
    latency_read_random_lifetime_max = Column(Float(30), nullable=True)
    latency_read_random_lifetime_median = Column(Float(30), nullable=True)
    latency_write_random_month_min = Column(Float(30), nullable=True)
    latency_write_random_month_25 = Column(Float(30), nullable=True)
    latency_write_random_month_75 = Column(Float(30), nullable=True)
    latency_write_random_month_max = Column(Float(30), nullable=True)
    latency_write_random_month_median = Column(Float(30), nullable=True)
    latency_write_random_year_min = Column(Float(30), nullable=True)
    latency_write_random_year_25 = Column(Float(30), nullable=True)
    latency_write_random_year_75 = Column(Float(30), nullable=True)
    latency_write_random_year_max = Column(Float(30), nullable=True)
    latency_write_random_year_median = Column(Float(30), nullable=True)
    latency_write_random_lifetime_min = Column(Float(30), nullable=True)
    latency_write_random_lifetime_25 = Column(Float(30), nullable=True)
    latency_write_random_lifetime_75 = Column(Float(30), nullable=True)
    latency_write_random_lifetime_max = Column(Float(30), nullable=True)
    latency_write_random_lifetime_median = Column(Float(30), nullable=True)


class Internalnetworkaggdata(Base):
    __tablename__ = 'xiaoice_internalnetworkaggdata'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    vm_id = Column(Integer, nullable=False)
    os_id = Column(Integer, nullable=False)
    single_threaded_throughput_month_min = Column(Float(30), nullable=True)
    single_threaded_throughput_month_25 = Column(Float(30), nullable=True)
    single_threaded_throughput_month_75 = Column(Float(30), nullable=True)
    single_threaded_throughput_month_max = Column(Float(30), nullable=True)
    single_threaded_throughput_month_median = Column(Float(30), nullable=True)
    single_threaded_throughput_year_min = Column(Float(30), nullable=True)
    single_threaded_throughput_year_25 = Column(Float(30), nullable=True)
    single_threaded_throughput_year_75 = Column(Float(30), nullable=True)
    single_threaded_throughput_year_max = Column(Float(30), nullable=True)
    single_threaded_throughput_year_median = Column(Float(30), nullable=True)
    single_threaded_throughput_lifetime_min = Column(Float(30), nullable=True)
    single_threaded_throughput_lifetime_25 = Column(Float(30), nullable=True)
    single_threaded_throughput_lifetime_75 = Column(Float(30), nullable=True)
    single_threaded_throughput_lifetime_max = Column(Float(30), nullable=True)
    single_threaded_throughput_lifetime_median = Column(Float(30), nullable=True)
    multi_threaded_throughput_month_min = Column(Float(30), nullable=True)
    multi_threaded_throughput_month_25 = Column(Float(30), nullable=True)
    multi_threaded_throughput_month_75 = Column(Float(30), nullable=True)
    multi_threaded_throughput_month_max = Column(Float(30), nullable=True)
    multi_threaded_throughput_month_median = Column(Float(30), nullable=True)
    multi_threaded_throughput_year_min = Column(Float(30), nullable=True)
    multi_threaded_throughput_year_25 = Column(Float(30), nullable=True)
    multi_threaded_throughput_year_75 = Column(Float(30), nullable=True)
    multi_threaded_throughput_year_max = Column(Float(30), nullable=True)
    multi_threaded_throughput_year_median = Column(Float(30), nullable=True)
    multi_threaded_throughput_lifetime_min = Column(Float(30), nullable=True)
    multi_threaded_throughput_lifetime_25 = Column(Float(30), nullable=True)
    multi_threaded_throughput_lifetime_75 = Column(Float(30), nullable=True)
    multi_threaded_throughput_lifetime_max = Column(Float(30), nullable=True)
    multi_threaded_throughput_lifetime_median = Column(Float(30), nullable=True)


# DB connection format: "engine://user:password@host:port/database"
Ignition = create_engine("mysql://%s:%s@%s:3306/%s" % (db_user, db_password, db_host, db_name))

# Create DB schema
Base.metadata.create_all(Ignition)
