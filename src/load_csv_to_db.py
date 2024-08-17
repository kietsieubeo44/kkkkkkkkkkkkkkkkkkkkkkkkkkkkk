import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from src.database import engine
from src.models import NetworkData

def load_csv_to_db(csv_file_path):
    try:
        # Đọc dữ liệu từ CSV
        df = pd.read_csv(csv_file_path)
        
        # Kết nối đến cơ sở dữ liệu
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Chuyển đổi DataFrame thành các đối tượng NetworkData và thêm vào cơ sở dữ liệu
        for _, row in df.iterrows():
            network_record = NetworkData(
                flow_duration=row['flow_duration'],
                Header_Length=row['Header_Length'],
                Protocol_Type=row['Protocol Type'],
                Duration=row['Duration'],
                Rate=row['Rate'],
                Srate=row['Srate'],
                Drate=row['Drate'],
                fin_flag_number=row['fin_flag_number'],
                syn_flag_number=row['syn_flag_number'],
                rst_flag_number=row['rst_flag_number'],
                psh_flag_number=row['psh_flag_number'],
                ack_flag_number=row['ack_flag_number'],
                ece_flag_number=row['ece_flag_number'],
                cwr_flag_number=row['cwr_flag_number'],
                ack_count=row['ack_count'],
                syn_count=row['syn_count'],
                fin_count=row['fin_count'],
                urg_count=row['urg_count'],
                rst_count=row['rst_count'],
                HTTP=row['HTTP'],
                HTTPS=row['HTTPS'],
                DNS=row['DNS'],
                Telnet=row['Telnet'],
                SMTP=row['SMTP'],
                SSH=row['SSH'],
                IRC=row['IRC'],
                TCP=row['TCP'],
                UDP=row['UDP'],
                DHCP=row['DHCP'],
                ARP=row['ARP'],
                ICMP=row['ICMP'],
                IPv=row['IPv'],
                LLC=row['LLC'],
                Tot_sum=row['Tot sum'],
                Min=row['Min'],
                Max=row['Max'],
                AVG=row['AVG'],
                Std=row['Std'],
                Tot_size=row['Tot size'],
                IAT=row['IAT'],
                Number=row['Number'],
                Magnitude=row['Magnitue'],
                Radius=row['Radius'],
                Covariance=row['Covariance'],
                Variance=row['Variance'],
                Weight=row['Weight'],
                label=row['label']
            )
            session.add(network_record)
        
        # Lưu các thay đổi và đóng kết nối
        session.commit()
        print("Data successfully loaded into the database.")
    
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

# Gọi hàm với đường dẫn tới file
