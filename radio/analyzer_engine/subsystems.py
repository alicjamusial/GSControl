import math
from resources import *


class Eps:
    EFFICIENCY_3V3 = 0.7
    EFFICIENCY_5V0 = 0.7


class Obc:
    FILE_FRAME_PAYLOAD = 232  # bytes (source: https://team.pw-sat.pl/w/obc/frames_format/)

    FLASH_POWER_CONSUMPTION = 0.1 # W

class Comm:
    DOWNLINK_POWER_CONSUMPTION = 3.0  # W
    DOWNLINK_MAX_PREAMBLE = Duration(0.4)
    DOWNLINK_MAX_PREAMBLE_9600 = Duration(0.3)
    UPLINK_PTT_DELAY = Duration(1.0)
    FULL_FRAME = 235  # bytes
    PROPAGATION_DELAY = Duration((2000.0/300000.0) * 2) # in both ways

    @classmethod
    def downlink_frames_duration(self, frames_count, bitrate):
        single_preamble = self.DOWNLINK_MAX_PREAMBLE
        if bitrate == 9600:
            single_preamble = self.DOWNLINK_MAX_PREAMBLE_9600

        preambles_duration = Duration(math.ceil(frames_count / 10.0) * float(single_preamble))

        duration = Duration(math.ceil(frames_count * (Comm.FULL_FRAME * 8.0) / bitrate))
        return duration + preambles_duration

    @classmethod
    def downlink_bytes_duration(self, bytes_count, bitrate):
        bits_count = (bytes_count) * 8
        tx_preamble = self.DOWNLINK_MAX_PREAMBLE
        if bitrate == 9600:
            tx_preamble = self.DOWNLINK_MAX_PREAMBLE_9600
        return Duration(float(bits_count) / bitrate) + tx_preamble + self.PROPAGATION_DELAY

    @classmethod
    def downlink_durations(self, frames_count):
        duration_1200 = float(self.downlink_frames_duration(frames_count, 1200))
        duration_2400 = float(self.downlink_frames_duration(frames_count, 2400))
        duration_4800 = float(self.downlink_frames_duration(frames_count, 4800))
        duration_9600 = float(self.downlink_frames_duration(frames_count, 9600))
        return Durations([duration_1200, duration_2400, duration_4800, duration_9600])

    @classmethod
    def downlink_energy_consumption(self, duration):
        return Energy((self.DOWNLINK_POWER_CONSUMPTION * float(duration) / 3600.0) * 1000.0)

    @classmethod
    def uplink_bytes_duration(self, bytes_count, bitrate):
        bits_count = bytes_count * 8
        return Duration(float(bits_count) / bitrate) + self.UPLINK_PTT_DELAY


class Camera:
    '''
    Resources utilization for Cameras.

    Source: PWSat2-SVN/system/tests_and_reports/29 -
            Experiments power consumption estimation/data/plots
    '''

    PHOTO_128_MAX_FULL_FRAMES = 12 # in FULL FRAMES (232 bytes each)
    PHOTO_240_MAX_FULL_FRAMES = 20 # in FULL FRAMES (232 bytes each)
    PHOTO_480_MAX_FULL_FRAMES = 80 # in FULL FRAMES (232 bytes each)

    COMMISSIONING_EXP_DURATION = Duration(230)
    COMMISSIONING_3V3_ENERGY_CONSUMPTION = Energy(0.0178 * 1000.0)

    CAMERA_POWER = 0.2618  # W

    PHOTO_128_TIME = 1.25  # s (max. val, about 25% greater than min)
    PHOTO_240_TIME = 4.7   # s (max. val, about 25% greater than min)
    PHOTO_480_TIME = 19    # s (max. val, about 25% greater than min)


class Pld:
    '''
    Resources utilization for Payload.

    Source: PWSat2-SVN/system/tests_and_reports/29 -
            Experiments power consumption estimation/data/plots
    '''

    SENS_5V0_ENERGY_CONSUMPTION = 0.0021 # Wh
    PLD_3V3_ENERGY_CONSUMPTION = 0.0178 # Wh

class Suns:
    EQUIPMENT_TURN_ON_TIME = 3  # s
    ESTIMATED_OBC_DELAY_PER_SAMPLE = 0.01  # s

    # W (source: https://team.pw-sat.pl/w/suns/suns_fm/power_consumption/)
    SUNS_EXP_AVERAGE_POWER_3V3 = 0.0701 
    
    # W (source: datasheet)
    SUNS_REF_AVERAGE_POWER_5V0 = 0.05  

    # W (source: https://team.pw-sat.pl/w/system/power-budget/experiments/#payload-commisioning - PLD SENS @ idle state)
    PLD_SENS_AVERAGE_POWER_5V0 = 5.0*0.0243  

class Radfet:
    RADFET_MEAN_POWER_5V0 = 0.2  # W (source PWSat2-SVN\system\tests_and_reports\23 - Power budget measurements\payload\SENS_5V)
    SUNS_REF_AVERAGE_POWER_5V0 = 0.05  # W (source: datasheet)

class Sads:
     # s (source: PWSat2-SVN\system\tests_and_reports\39 - SADS with load)
    EXPERIMENT_DURATION = 290 

    # Wh (source: PWSat2-SVN\system\tests_and_reports\39 - SADS with load)
    EXPERIMENT_ENERGY_CONSUMPTION = 0.1293 

class Sail:
    SAIL_TK_POWER = 2  # W
    SAIL_EXP_DURATION = 240  # s (source: OBC code)
    SUNS_REF_AVERAGE_POWER_5V0 = 0.05
    PLD_SENS_AVERAGE_POWER_5V0 = 5.0*0.0243

class Adcs:
    MEAN_POWER_CONSUMPTION = 0.3 # W
