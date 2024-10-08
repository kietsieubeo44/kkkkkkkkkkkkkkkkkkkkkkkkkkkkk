from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NetworkData(Base):
    __tablename__ = 'network_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    flow_duration = Column(Float)
    Header_Length = Column(Float)
    Protocol_Type = Column(String(50))
    Duration = Column(Float)
    Rate = Column(Float)
    Srate = Column(Float)
    Drate = Column(Float)
    fin_flag_number = Column(Integer)
    syn_flag_number = Column(Integer)
    rst_flag_number = Column(Integer)
    psh_flag_number = Column(Integer)
    ack_flag_number = Column(Integer)
    ece_flag_number = Column(Integer)
    cwr_flag_number = Column(Integer)
    ack_count = Column(Integer)
    syn_count = Column(Integer)
    fin_count = Column(Integer)
    urg_count = Column(Integer)
    rst_count = Column(Integer)
    HTTP = Column(Float)
    HTTPS = Column(Float)
    DNS = Column(Float)
    Telnet = Column(Float)
    SMTP = Column(Float)
    SSH = Column(Float)
    IRC = Column(Float)
    TCP = Column(Float)
    UDP = Column(Float)
    DHCP = Column(Float)
    ARP = Column(Float)
    ICMP = Column(Float)
    IPv = Column(Float)
    LLC = Column(Float)
    Tot_sum = Column(Float)
    Min = Column(Float)
    Max = Column(Float)
    AVG = Column(Float)
    Std = Column(Float)
    Tot_size = Column(Float)
    IAT = Column(Float)
    Number = Column(Integer)
    Magnitude = Column(Float)
    Radius = Column(Float)
    Covariance = Column(Float)
    Variance = Column(Float)
    Weight = Column(Float)
    label = Column(String(50))
