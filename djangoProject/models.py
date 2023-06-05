from django.db import models


class Auxiliarytool(models.Model):
    tool_id = models.DecimalField(db_column='Tool_ID', primary_key=True, max_digits=10,
                                  decimal_places=0)  # Field name made lowercase.
    tool_name = models.CharField(db_column='Tool_Name', max_length=50,
                                 db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    min_size = models.CharField(db_column='Min_Size', max_length=20,
                                db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuxiliaryTool'
        app_label = 'djangoProject'


class User(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,
                            db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    genders = models.CharField(db_column='Genders', max_length=10,
                               db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    birthday = models.DateField(db_column='Birthday')  # Field name made lowercase.
    certificate_number = models.CharField(db_column='Certificate_Number', max_length=50,
                                          db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    certificate_expiry_date = models.DateField(db_column='Certificate_Expiry_Date')  # Field name made lowercase.
    disability_level = models.DecimalField(db_column='Disability_Level', max_digits=10,
                                           decimal_places=0)  # Field name made lowercase.
    disability_category = models.CharField(db_column='Disability_Category', max_length=20,
                                           db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100,
                               db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='utf8mb3_general_ci', blank=True,
                             null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='utf8mb3_general_ci', blank=True,
                             null=True)  # Field name made lowercase.
    contact_person_phone = models.CharField(db_column='Contact_Person_Phone', max_length=20,
                                            db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    contact_relationship = models.CharField(db_column='Contact_Relationship', max_length=20,
                                            db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20,
                                db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30,
                                db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    auxiliary_tool = models.ForeignKey(Auxiliarytool, models.DO_NOTHING, db_column='Auxiliary_tool', blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'
        app_label = 'djangoProject'

class Driver(models.Model):
    driver_id = models.AutoField(db_column='Driver_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    driver_license_number = models.CharField(db_column='Driver_License_Number', max_length=30, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    manger = models.ForeignKey('Managers', models.DO_NOTHING, db_column='Manger_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'djangoProject'
        db_table = 'Driver'


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
        app_label = 'djangoProject'

