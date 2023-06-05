from django.db import models


# Create your models here.
class Managers(models.Model):
    manager_id = models.AutoField(db_column='Manager_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,
                            db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20,
                             db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20,
                                db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Managers'
        app_label = 'driver'


class CheckList(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tire_pressure1 = models.DecimalField(db_column='Tire_Pressure1', max_digits=10, decimal_places=0, blank=True,
                                         null=True)  # Field name made lowercase.
    tire_pressure2 = models.DecimalField(db_column='Tire_Pressure2', max_digits=10, decimal_places=0, blank=True,
                                         null=True)  # Field name made lowercase.
    tire_pressure3 = models.DecimalField(db_column='Tire_Pressure3', max_digits=10, decimal_places=0, blank=True,
                                         null=True)  # Field name made lowercase.
    tire_pressure4 = models.DecimalField(db_column='Tire_Pressure4', max_digits=10, decimal_places=0, blank=True,
                                         null=True)  # Field name made lowercase.
    engine_oil = models.DecimalField(db_column='Engine_Oil', max_digits=10, decimal_places=0, blank=True,
                                     null=True)  # Field name made lowercase.
    directional_motor_oil = models.DecimalField(db_column='Directional_Motor_Oil', max_digits=10, decimal_places=0,
                                                blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'driver'
        db_table = 'Check_List'


class Report(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    real_income = models.IntegerField(db_column='Real_Income')  # Field name made lowercase.
    real_passenger = models.IntegerField(db_column='Real_Passenger')  # Field name made lowercase.
    schedule = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='Schedule')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'driver'
        db_table = 'Report'


class Route(models.Model):
    route_id = models.AutoField(db_column='Route_ID', primary_key=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100,
                               db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    schedule = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='Schedule')  # Field name made lowercase.
    manager = models.ForeignKey(Managers, models.DO_NOTHING, db_column='Manager_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'driver'
        db_table = 'Route'


class Driver(models.Model):
    driver_id = models.AutoField(db_column='Driver_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,
                            db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20,
                             db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    driver_license_number = models.CharField(db_column='Driver_License_Number', max_length=30,
                                             db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30,
                                db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    manger = models.ForeignKey('Managers', models.DO_NOTHING, db_column='Manger_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'driver'
        db_table = 'Driver'


class Schedule(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    driver = models.ForeignKey(Driver, models.DO_NOTHING, db_column='Driver')  # Field name made lowercase.
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='Vehicle')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    start_mileage = models.DecimalField(db_column='Start_Mileage', max_digits=10, decimal_places=0, blank=True,
                                        null=True)  # Field name made lowercase.
    end_mileage = models.DecimalField(db_column='End_Mileage', max_digits=10, decimal_places=0, blank=True,
                                      null=True)  # Field name made lowercase.
    should_charge = models.DecimalField(db_column='Should_Charge', max_digits=10,
                                        decimal_places=0)  # Field name made lowercase.
    car_check_list = models.ForeignKey(CheckList, models.DO_NOTHING,
                                       db_column='Car_Check_List')  # Field name made lowercase.
    manager = models.ForeignKey(Managers, models.DO_NOTHING, db_column='Manager')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'driver'
        db_table = 'Schedule'


class Vehicle(models.Model):
    vehicles_id = models.AutoField(db_column='Vehicles_ID', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50,
                                db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    car_number = models.CharField(db_column='Car_Number', max_length=10,
                                  db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    can_wheelchair = models.IntegerField(db_column='Can_Wheelchair')  # Field name made lowercase.
    passenger_number = models.IntegerField(db_column='Passenger_Number')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'driver'
        db_table = 'Vehicle'
