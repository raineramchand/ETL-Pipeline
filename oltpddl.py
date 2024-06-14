import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('newhotel.db')

# Create a cursor object
c = conn.cursor()

# Execute DDL statements to create tables with updated schema
c.execute('''
CREATE TABLE Guests (
    GuestID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Email TEXT NOT NULL,
    PhoneNumber TEXT NOT NULL,
    DateOfBirth TEXT,
    Country TEXT,
    VIPStatus BOOLEAN
)
''')

c.execute('''
CREATE TABLE Rooms (
    RoomID INTEGER PRIMARY KEY,
    RoomType TEXT NOT NULL,
    PricePerNight REAL NOT NULL,
    Status TEXT CHECK(Status IN ('Available', 'Occupied', 'Maintenance')),
    FloorNumber INTEGER
)
''')

c.execute('''
CREATE TABLE Bookings (
    BookingID INTEGER PRIMARY KEY,
    GuestID INTEGER,
    RoomID INTEGER,
    CheckInDate TEXT NOT NULL,
    CheckOutDate TEXT NOT NULL,
    NumberOfGuests INTEGER,
    TotalBill REAL,
    Discounts REAL,
    FOREIGN KEY (GuestID) REFERENCES Guests (GuestID),
    FOREIGN KEY (RoomID) REFERENCES Rooms (RoomID)
)
''')

c.execute('''
CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Position TEXT NOT NULL,
    HireDate TEXT NOT NULL,
    Salary REAL,
    Department TEXT CHECK(Department IN ('Administration', 'Housekeeping', 'Kitchen', 'Front Desk')),
    PerformanceRating INTEGER CHECK(PerformanceRating BETWEEN 1 AND 10)
)
''')

c.execute('''
CREATE TABLE Services (
    ServiceID INTEGER PRIMARY KEY,
    ServiceType TEXT NOT NULL,
    ServiceName TEXT NOT NULL,
    Price REAL NOT NULL,
    Cost REAL,
    PopularTimes TEXT
)
''')

c.execute('''
CREATE TABLE ServiceBookings (
    ServiceBookingID INTEGER PRIMARY KEY,
    BookingID INTEGER,
    ServiceID INTEGER,
    Date TEXT NOT NULL,
    Time TEXT NOT NULL,
    Quantity INTEGER,
    TotalServiceCost REAL,
    FOREIGN KEY (BookingID) REFERENCES Bookings (BookingID),
    FOREIGN KEY (ServiceID) REFERENCES Services (ServiceID)
)
''')

c.execute('''
CREATE TABLE Payments (
    PaymentID INTEGER PRIMARY KEY,
    BookingID INTEGER,
    PaymentDate TEXT NOT NULL,
    PaymentMethod TEXT NOT NULL,
    AmountPaid REAL NOT NULL,
    AmountDue REAL,
    Revenue REAL,
    OutstandingBalance REAL,
    FOREIGN KEY (BookingID) REFERENCES Bookings (BookingID)
)
''')

c.execute('''
CREATE TABLE Reviews (
    ReviewID INTEGER PRIMARY KEY,
    BookingID INTEGER,
    Rating INTEGER NOT NULL,
    Review TEXT NOT NULL,
    GuestFeedback TEXT,
    StaffRating INTEGER CHECK(StaffRating BETWEEN 1 AND 5),
    FOREIGN KEY (BookingID) REFERENCES Bookings (BookingID)
)
''')

c.execute('''
CREATE TABLE RoomMaintenance (
    MaintenanceID INTEGER PRIMARY KEY,
    RoomID INTEGER,
    EmployeeID INTEGER,
    MaintenanceDate TEXT NOT NULL,
    LastMaintenanceDate TEXT,
    Issue NOT NULL,
    Status TEXT NOT NULL CHECK(Status IN ('Pending', 'In Progress', 'Completed')),
    CostofMaintenance REAL,
    Duration INTEGER,  -- Duration in hours
    FOREIGN KEY (RoomID) REFERENCES Rooms (RoomID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees (EmployeeID)
)
''')

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
