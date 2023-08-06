from pydantic import BaseModel


class ModelInputs(BaseModel):
    brand : str
    model : str
    year : float
    mileage : float
    engine : str
    engine_size : float
    transmission : str
    automatic_transmission : float
    fuel_type : str
    drivetrain : str
    min_mpg : float
    max_mpg : float
    damaged : float
    first_owner : float
    personal_using : float
    turbo : float
    alloy_wheels : float
    adaptive_cruise_control : float
    navigation_system : float
    power_liftgate : float
    backup_camera : float
    keyless_start : float
    remote_start : float
    sunroofmoonroof : float
    automatic_emergency_braking : float
    stability_control : float
    leather_seats : float
    memory_seat : float
    third_row_seating : float
    apple_car_playandroid_auto : float
    bluetooth : float
    usb_port : float
    heated_seats : float
    interior_color : str
    exterior_color : str