from django.db import models

# Create your models here.

class Auxiliarytool(models.Model):
    tool_id = models.DecimalField(db_column='Tool_ID', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    tool_name = models.CharField(db_column='Tool_Name', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    min_size = models.CharField(db_column='Min_Size', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuxiliaryTool'
        app_label = 'User'

class User(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    genders = models.CharField(db_column='Genders', max_length=10, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    birthday = models.DateField(db_column='Birthday')  # Field name made lowercase.
    certificate_number = models.CharField(db_column='Certificate_Number', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    certificate_expiry_date = models.DateField(db_column='Certificate_Expiry_Date')  # Field name made lowercase.
    disability_level = models.DecimalField(db_column='Disability_Level', max_digits=10, decimal_places=0)  # Field name made lowercase.
    disability_category = models.CharField(db_column='Disability_Category', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    contact_person_phone = models.CharField(db_column='Contact_Person_Phone', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    contact_relationship = models.CharField(db_column='Contact_Relationship', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    auxiliary_tool = models.ForeignKey(Auxiliarytool, models.DO_NOTHING, db_column='Auxiliary_tool', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'
        app_label = 'User'


class Managers(models.Model):
    manager_id = models.AutoField(db_column='Manager_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Managers'
        app_label = 'User'

class Driver(models.Model):
    driver_id = models.AutoField(db_column='Driver_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    driver_license_number = models.CharField(db_column='Driver_License_Number', max_length=30, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    manger = models.ForeignKey('Managers', models.DO_NOTHING, db_column='Manger_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Driver'
        app_label = 'User'

class CheckList(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tire_pressure1 = models.DecimalField(db_column='Tire_Pressure1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tire_pressure2 = models.DecimalField(db_column='Tire_Pressure2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tire_pressure3 = models.DecimalField(db_column='Tire_Pressure3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tire_pressure4 = models.DecimalField(db_column='Tire_Pressure4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    engine_oil = models.DecimalField(db_column='Engine_Oil', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    directional_motor_oil = models.DecimalField(db_column='Directional_Motor_Oil', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'User'
        db_table = 'Check_List'
class Vehicle(models.Model):
    vehicles_id = models.AutoField(db_column='Vehicles_ID', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    car_number = models.CharField(db_column='Car_Number', max_length=10, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    can_wheelchair = models.IntegerField(db_column='Can_Wheelchair')  # Field name made lowercase.
    passenger_number = models.IntegerField(db_column='Passenger_Number')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Check_List'
        app_label = 'User'

class Schedule(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    driver = models.ForeignKey(Driver, models.DO_NOTHING, db_column='Driver')  # Field name made lowercase.
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='Vehicle')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    start_mileage = models.DecimalField(db_column='Start_Mileage', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    end_mileage = models.DecimalField(db_column='End_Mileage', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    should_charge = models.DecimalField(db_column='Should_Charge', max_digits=10, decimal_places=0)  # Field name made lowercase.
    car_check_list = models.ForeignKey(CheckList, models.DO_NOTHING, db_column='Car_Check_List')  # Field name made lowercase.
    manager = models.ForeignKey(Managers, models.DO_NOTHING, db_column='Manager')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedule'
        app_label = 'User'


class Appointment(models.Model):
    appointment_id = models.AutoField(db_column='Appointment_ID', primary_key=True)  # Field name made lowercase.
    appointment_user = models.ForeignKey('User', models.DO_NOTHING, db_column='Appointment_User')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    escorts = models.IntegerField(db_column='Escorts')  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='utf8mb3_general_ci', null=True)  # Field name made lowercase.
    schedules = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='Schedules_ID', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    manager = models.ForeignKey('Managers', models.DO_NOTHING, db_column='Manager_ID', blank=True, null=True)  # Field name made lowercase.
    should_pay = models.IntegerField(
        db_column='Should_Pay',
        max_length=99999,
        null=True,
        blank=True
    )
    mileage = models.DecimalField(
        db_column='Mileage',
        decimal_places=2,
        max_digits=2,
        null=True,
        blank=True
    )
    class Meta:
        managed = False
        db_table = 'Appointment'
        app_label = 'User'

