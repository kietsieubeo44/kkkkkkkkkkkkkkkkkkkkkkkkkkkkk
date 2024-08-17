from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Thay đổi thông tin kết nối cơ sở dữ liệu theo thông tin bạn đã cung cấp
DATABASE_URL = "mysql+pymysql://admin:lmht456kiet123@localhost/my_database"

# Tạo engine và session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
