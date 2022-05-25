from Flory.FloryProprietaryB_65285 import FloryProprietaryB_65285
from J1939.ActiveDiagnosticTroubleCodes_65226 import ActiveDiagnosticTroubleCodes_65226
from J1939.AfterTreatment1DieselExhaustFluidTank_65110 import AfterTreatment1DieselExhaustFluidTank_65110
from Consts import FLORY_VEHICLE_PRODUCT_LINE_MESSAGE_PGN
from J1939.DashDisplay1_65276 import DashDisplay1_65276
from J1939.ElectronicEngineController1_61444 import ElectronicEngineController1_61444
from J1939.EngineFluidLevelPressure1_65263 import EngineFluidLevelPressure1_65263
from J1939.EngineFluidLevelPressure2_65243 import EngineFluidLevelPressure2_65243
from J1939.EngineHoursRevolutions_65253 import EngineHoursRevolutions_65253
from J1939.EngineTemperature1_65262 import EngineTemperature1_65262
from Flory.FloryProprietaryA_61184 import FloryProprietaryA_61184
from J1939.FuelEconomyLiquid_65266 import FuelEconomyLiquid_65266
from J1939.IntakeExhaustConditions1_65270 import IntakeExhaustConditions1_65270
from J1939.CruiseControlVehicleSpeed1_65265 import CruiseControlVehicleSpeed1_65265
from OMC.OmcShakerActivity_65411 import OmcShakerActivity_65411
from Flory.FloryProprietaryB_65280 import FloryProprietaryB_65280
from Flory.FloryProprietaryB_65281 import FloryProprietaryB65281
from Flory.FloryProprietaryB_65282 import FloryProprietaryB_65282
from Flory.FloryProprietaryB_65283 import FloryProprietaryB_65283
from Flory.FloryProprietaryB_65284 import FloryProprietaryB_65284
from J1939.ServiceInformation_65216 import ServiceInformation_65216
from J1939.VehicleDirectionSpeed_65256 import VehicleDirectionSpeed_65256
from J1939.VehicleElectricalPower1_65271 import VehicleElectricalPower1_65271
from J1939.VehicleIdentification_65260 import VehicleIdentification_65260


class FloryCanbusMessageFactory:

    @staticmethod
    def create_message(pgn, data):
        if pgn == FLORY_VEHICLE_PRODUCT_LINE_MESSAGE_PGN:
            return FloryProprietaryA_61184(pgn, data)
        if pgn == '61444':  # Electronic Engine Controller 1
            return ElectronicEngineController1_61444(pgn, data)
        if pgn == '65110':  # After Treatment 1 Diesel Exhaust Fluid Tank
            return AfterTreatment1DieselExhaustFluidTank_65110(pgn, data)
        if pgn == '65226':  # Active Diagnostic Trouble Codes
            return ActiveDiagnosticTroubleCodes_65226(pgn, data)
        if pgn == '65271':  # Vehicle Electrical Power 1
            return VehicleElectricalPower1_65271(pgn, data)
        if pgn == '65243':  # Engine Fluid Level/Pressure 2
            return EngineFluidLevelPressure2_65243(pgn, data)
        if pgn == '65253':  # Engine Hours, Revolutions
            return EngineHoursRevolutions_65253(pgn, data)
        if pgn == '65256':  # Vehicle Direction/Speed
            return VehicleDirectionSpeed_65256(pgn, data)
        if pgn == '65265':  # Cruise Control/Vehicle Speed 1
            return CruiseControlVehicleSpeed1_65265(pgn, data)
        if pgn == '65260':  # Vehicle Identification
            return VehicleIdentification_65260(pgn, data)
        if pgn == '65266':  # Fuel Economy (Liquid)
            return FuelEconomyLiquid_65266(pgn, data)
        if pgn == '65216':  # Service Information
            return ServiceInformation_65216(pgn, data)
        if pgn == '65262':  # Engine Temperature 1
            return EngineTemperature1_65262(pgn, data)
        if pgn == '65263':  # Engine Fluid Level/Pressure 1
            return EngineFluidLevelPressure1_65263(pgn, data)
        if pgn == '65270':  # Intake/Exhaust Conditions 1
            return IntakeExhaustConditions1_65270(pgn, data)
        if pgn == '65276':  # Dash Display 1
            return DashDisplay1_65276(pgn, data)
        if pgn == '65280':
            return FloryProprietaryB_65280(pgn, data)
        if pgn == '65281':
            return FloryProprietaryB65281(pgn, data)
        if pgn == '65282':
            return FloryProprietaryB_65282(pgn, data)
        if pgn == '65283':
            return FloryProprietaryB_65283(pgn, data)
        if pgn == '65284':
            return FloryProprietaryB_65284(pgn, data)
        if pgn == '65285':
            return FloryProprietaryB_65285(pgn, data)
        if pgn == '65411':
            return OmcShakerActivity_65411(pgn, data)


        return None

