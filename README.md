# LTCBusAppointment_DjangoWeb

### User

-   入口登入： /user
-   帳號註冊： /user/register
-   修改資料： /user/edit
-   管理預約： /user/appointment_all
-   新增預約： /user/appointment_create

### Driver

-   入口登入： /driver	
-   查看班表： /driver/schedule_table
-   回報資料： /driver/report_form/<schedule_id>
-   查看路線： /route_table/<schedule_id>

### Manager

-   入口登入： /manager
-   管理司機： /manager/mgdriver
-   新增司機： /manager/registerDriver
-   管理使用者：/manager/mguser
-   編輯司機資料：/manager/editDriver/<driver_id>
-   管理預約： /manager/mgappointment
-   排班/編輯預約： /manager/editAppointment/<schedule_id>
-   統計資料：/manager/statistic

