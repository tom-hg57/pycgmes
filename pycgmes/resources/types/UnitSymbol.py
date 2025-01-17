"""
Generated from the CGMES files via cimgen: https://github.com/sogno-platform/cimgen
"""

from enum import Enum


class UnitSymbol(str, Enum):
    """
    The derived units defined for usage in the CIM. In some cases, the derived unit is equal to an SI unit. Whenever
      possible, the standard derived symbol is used instead of the formula for the derived unit. For example, the
      unit symbol Farad is defined as "F" instead of "CPerV". In cases where a standard symbol does not exist for a
      derived unit, the formula for the unit is used as the unit symbol. For example, density does not have a
      standard symbol and so it is represented as "kgPerm3". With the exception of the "kg", which is an SI unit,
      the unit symbols do not contain multipliers and therefore represent the base derived unit to which a
      multiplier can be applied as a whole.  Every unit symbol is treated as an unparseable text as if it were a
      single-letter symbol. The meaning of each unit symbol is defined by the accompanying descriptive text and not
      by the text contents of the unit symbol. To allow the widest possible range of serializations without
      requiring special character handling, several substitutions are made which deviate from the format described
      in IEC 80000-1. The division symbol "/" is replaced by the letters "Per". Exponents are written in plain text
      after the unit as "m3" instead of being formatted as "m" with a superscript of 3  or introducing a symbol as
      in "m^3". The degree symbol "[SYMBOL REMOVED]" is replaced with the letters "deg". Any clarification of the
      meaning for a substitution is included in the description for the unit symbol. Non-SI units are included in
      list of unit symbols to allow sources of data to be correctly labelled with their non-SI units (for example, a
      GPS sensor that is reporting numbers that represent feet instead of meters). This allows software to use the
      unit symbol information correctly convert and scale the raw data of those sources into SI-based units.  The
      integer values are used for harmonization with IEC 61850.
    """

    none = "none"  # Dimension less quantity, e.g. count, per unit, etc.  # noqa: E501, E741, RUF003
    m = "m"  # Length in metres.  # noqa: E501, E741, RUF003
    kg = "kg"  # Mass in kilograms.  Note: multiplier &quot;k&quot; is included in this unit symbol for compatibility with IEC 61850-7-3.  # noqa: E501, E741, RUF003
    s = "s"  # Time in seconds.  # noqa: E501, E741, RUF003
    A = "A"  # Current in amperes.  # noqa: E501, E741, RUF003
    K = "K"  # Temperature in kelvins.  # noqa: E501, E741, RUF003
    mol = "mol"  # Amount of substance in moles.  # noqa: E501, E741, RUF003
    cd = "cd"  # Luminous intensity in candelas.  # noqa: E501, E741, RUF003
    deg = "deg"  # Plane angle in degrees.  # noqa: E501, E741, RUF003
    rad = "rad"  # Plane angle in radians (m/m).  # noqa: E501, E741, RUF003
    sr = "sr"  # Solid angle in steradians (m2/m2).  # noqa: E501, E741, RUF003
    Gy = "Gy"  # Absorbed dose in grays (J/kg).  # noqa: E501, E741, RUF003
    Bq = "Bq"  # Radioactivity in becquerels (1/s).  # noqa: E501, E741, RUF003
    degC = "degC"  # Relative temperature in degrees Celsius. In the SI unit system the symbol is [SYMBOL REMOVED]C. Electric charge is measured in coulomb that has the unit symbol C. To distinguish degree Celsius from coulomb the symbol used in the UML is degC. The reason for not using [SYMBOL REMOVED]C is that the special character [SYMBOL REMOVED] is difficult to manage in software.  # noqa: E501, E741, RUF003
    Sv = "Sv"  # Dose equivalent in sieverts (J/kg).  # noqa: E501, E741, RUF003
    F = "F"  # Electric capacitance in farads (C/V).  # noqa: E501, E741, RUF003
    C = "C"  # Electric charge in coulombs (A·s).  # noqa: E501, E741, RUF003
    S = "S"  # Conductance in siemens.  # noqa: E501, E741, RUF003
    H = "H"  # Electric inductance in henrys (Wb/A).  # noqa: E501, E741, RUF003
    V = "V"  # Electric potential in volts (W/A).  # noqa: E501, E741, RUF003
    ohm = "ohm"  # Electric resistance in ohms (V/A).  # noqa: E501, E741, RUF003
    J = "J"  # Energy in joules (N·m = C·V = W·s).  # noqa: E501, E741, RUF003
    N = "N"  # Force in newtons (kg·m/s²).  # noqa: E501, E741, RUF003
    Hz = "Hz"  # Frequency in hertz (1/s).  # noqa: E501, E741, RUF003
    lx = "lx"  # Illuminance in lux (lm/m²).  # noqa: E501, E741, RUF003
    lm = "lm"  # Luminous flux in lumens (cd·sr).  # noqa: E501, E741, RUF003
    Wb = "Wb"  # Magnetic flux in webers (V·s).  # noqa: E501, E741, RUF003
    T = "T"  # Magnetic flux density in teslas (Wb/m2).  # noqa: E501, E741, RUF003
    W = "W"  # Real power in watts (J/s). Electrical power may have real and reactive components. The real portion of electrical power (I&amp;#178;R or VIcos(phi)), is expressed in Watts. See also apparent power and reactive power.  # noqa: E501, E741, RUF003
    Pa = "Pa"  # Pressure in pascals (N/m²). Note: the absolute or relative measurement of pressure is implied with this entry. See below for more explicit forms.  # noqa: E501, E741, RUF003
    m2 = "m2"  # Area in square metres (m²).  # noqa: E501, E741, RUF003
    m3 = "m3"  # Volume in cubic metres (m³).  # noqa: E501, E741, RUF003
    mPers = "mPers"  # Velocity in metres per second (m/s).  # noqa: E501, E741, RUF003
    mPers2 = "mPers2"  # Acceleration in metres per second squared (m/s²).  # noqa: E501, E741, RUF003
    m3Pers = "m3Pers"  # Volumetric flow rate in cubic metres per second (m³/s).  # noqa: E501, E741, RUF003
    mPerm3 = "mPerm3"  # Fuel efficiency in metres per cubic metres (m/m³).  # noqa: E501, E741, RUF003
    kgm = "kgm"  # Moment of mass in kilogram metres (kg·m) (first moment of mass). Note: multiplier &quot;k&quot; is included in this unit symbol for compatibility with IEC 61850-7-3.  # noqa: E501, E741, RUF003
    kgPerm3 = "kgPerm3"  # Density in kilogram/cubic metres (kg/m³). Note: multiplier &quot;k&quot; is included in this unit symbol for compatibility with IEC 61850-7-3.  # noqa: E501, E741, RUF003
    m2Pers = "m2Pers"  # Viscosity in square metres / second (m²/s).  # noqa: E501, E741, RUF003
    WPermK = "WPermK"  # Thermal conductivity in watt/metres kelvin.  # noqa: E501, E741, RUF003
    JPerK = "JPerK"  # Heat capacity in joules/kelvin.  # noqa: E501, E741, RUF003
    ppm = "ppm"  # Concentration in parts per million.  # noqa: E501, E741, RUF003
    rotPers = "rotPers"  # Rotations per second (1/s). See also Hz (1/s).  # noqa: E501, E741, RUF003
    radPers = "radPers"  # Angular velocity in radians per second (rad/s).  # noqa: E501, E741, RUF003
    WPerm2 = "WPerm2"  # Heat flux density, irradiance, watts per square metre.  # noqa: E501, E741, RUF003
    JPerm2 = "JPerm2"  # Insulation energy density, joules per square metre or watt second per square metre.  # noqa: E501, E741, RUF003
    SPerm = "SPerm"  # Conductance per length (F/m).  # noqa: E501, E741, RUF003
    KPers = "KPers"  # Temperature change rate in kelvins per second.  # noqa: E501, E741, RUF003
    PaPers = "PaPers"  # Pressure change rate in pascals per second.  # noqa: E501, E741, RUF003
    JPerkgK = "JPerkgK"  # Specific heat capacity, specific entropy, joules per kilogram Kelvin.  # noqa: E501, E741, RUF003
    VA = "VA"  # Apparent power in volt amperes. See also real power and reactive power.  # noqa: E501, E741, RUF003
    VAr = "VAr"  # Reactive power in volt amperes reactive. The &quot;reactive&quot; or &quot;imaginary&quot; component of electrical power (VIsin(phi)). (See also real power and apparent power). Note: Different meter designs use different methods to arrive at their results. Some meters may compute reactive power as an arithmetic value, while others compute the value vectorially. The data consumer should determine the method in use and the suitability of the measurement for the intended purpose.  # noqa: E501, E741, RUF003
    cosPhi = "cosPhi"  # Power factor, dimensionless. Note 1: This definition of power factor only holds for balanced systems. See the alternative definition under code 153. Note 2 : Beware of differing sign conventions in use between the IEC and EEI. It is assumed that the data consumer understands the type of meter in use and the sign convention in use by the utility.  # noqa: E501, E741, RUF003
    Vs = "Vs"  # Volt seconds (Ws/A).  # noqa: E501, E741, RUF003
    V2 = "V2"  # Volt squared (W²/A²).  # noqa: E501, E741, RUF003
    As = "As"  # Ampere seconds (A·s).  # noqa: E501, E741, RUF003
    A2 = "A2"  # Amperes squared (A²).  # noqa: E501, E741, RUF003
    A2s = "A2s"  # Ampere squared time in square amperes (A²s).  # noqa: E501, E741, RUF003
    VAh = "VAh"  # Apparent energy in volt ampere hours.  # noqa: E501, E741, RUF003
    Wh = "Wh"  # Real energy in watt hours.  # noqa: E501, E741, RUF003
    VArh = "VArh"  # Reactive energy in volt ampere reactive hours.  # noqa: E501, E741, RUF003
    VPerHz = "VPerHz"  # Magnetic flux in volt per hertz.  # noqa: E501, E741, RUF003
    HzPers = "HzPers"  # Rate of change of frequency in hertz per second.  # noqa: E501, E741, RUF003
    character = "character"  # Number of characters.  # noqa: E501, E741, RUF003
    charPers = "charPers"  # Data rate (baud) in characters per second.  # noqa: E501, E741, RUF003
    kgm2 = "kgm2"  # Moment of mass in kilogram square metres (kg·m²) (Second moment of mass, commonly called the moment of inertia). Note: multiplier &quot;k&quot; is included in this unit symbol for compatibility with IEC 61850-7-3.  # noqa: E501, E741, RUF003
    dB = "dB"  # Sound pressure level in decibels. Note:  multiplier &quot;d&quot; is included in this unit symbol for compatibility with IEC 61850-7-3.  # noqa: E501, E741, RUF003
    WPers = "WPers"  # Ramp rate in watts per second.  # noqa: E501, E741, RUF003
    lPers = "lPers"  # Volumetric flow rate in litres per second.  # noqa: E501, E741, RUF003
    dBm = "dBm"  # Power level (logarithmic ratio of signal strength , Bel-mW), normalized to 1mW. Note:  multiplier &quot;d&quot; is included in this unit symbol for compatibility with IEC 61850-7-3.  # noqa: E501, E741, RUF003
    h = "h"  # Time in hours, hour = 60 min = 3600 s.  # noqa: E501, E741, RUF003
    min = "min"  # Time in minutes, minute  = 60 s.  # noqa: E501, E741, RUF003
    Q = "Q"  # Quantity power, Q.  # noqa: E501, E741, RUF003
    Qh = "Qh"  # Quantity energy, Qh.  # noqa: E501, E741, RUF003
    ohmm = "ohmm"  # Resistivity, ohm metres, (rho).  # noqa: E501, E741, RUF003
    APerm = "APerm"  # A/m, magnetic field strength, amperes per metre.  # noqa: E501, E741, RUF003
    V2h = "V2h"  # Volt-squared hour, volt-squared-hours.  # noqa: E501, E741, RUF003
    A2h = "A2h"  # Ampere-squared hour, ampere-squared hour.  # noqa: E501, E741, RUF003
    Ah = "Ah"  # Ampere-hours, ampere-hours.  # noqa: E501, E741, RUF003
    count = "count"  # Amount of substance, Counter value.  # noqa: E501, E741, RUF003
    ft3 = "ft3"  # Volume, cubic feet.  # noqa: E501, E741, RUF003
    m3Perh = "m3Perh"  # Volumetric flow rate, cubic metres per hour.  # noqa: E501, E741, RUF003
    gal = "gal"  # Volume in gallons, US gallon (1 gal = 231 in3 = 128 fl ounce).  # noqa: E501, E741, RUF003
    Btu = "Btu"  # Energy, British Thermal Units.  # noqa: E501, E741, RUF003
    l = "l"  # Volume in litres, litre = dm3 = m3/1000.  # noqa: E501, E741, RUF003
    lPerh = "lPerh"  # Volumetric flow rate, litres per hour.  # noqa: E501, E741, RUF003
    lPerl = "lPerl"  # Concentration, The ratio of the volume of a solute divided by the volume of  the solution. Note: Users may need use a prefix such a ‘µ' to express a quantity such as ‘µL/L'.  # noqa: E501, E741, RUF003
    gPerg = "gPerg"  # Concentration, The ratio of the mass of a solute divided by the mass of  the solution. Note: Users may need use a prefix such a ‘µ' to express a quantity such as ‘µg/g'.  # noqa: E501, E741, RUF003
    molPerm3 = "molPerm3"  # Concentration, The amount of substance concentration, (c), the amount of solvent in moles divided by the volume of solution in m³.  # noqa: E501, E741, RUF003
    molPermol = "molPermol"  # Concentration, Molar fraction, the ratio of the molar amount of a solute divided by the molar amount of the solution.  # noqa: E501, E741, RUF003
    molPerkg = "molPerkg"  # Concentration, Molality, the amount of solute in moles and the amount of solvent in kilograms.  # noqa: E501, E741, RUF003
    sPers = "sPers"  # Time, Ratio of time.  Note: Users may need to supply a prefix such as ‘&amp;#181;' to show rates such as ‘&amp;#181;s/s'.  # noqa: E501, E741, RUF003
    HzPerHz = "HzPerHz"  # Frequency, rate of frequency change.   Note: Users may need to supply a prefix such as ‘m' to show rates such as ‘mHz/Hz'.  # noqa: E501, E741, RUF003
    VPerV = "VPerV"  # Voltage, ratio of voltages.  Note: Users may need to supply a prefix such as ‘m' to show rates such as ‘mV/V'.  # noqa: E501, E741, RUF003
    APerA = "APerA"  # Current, ratio of amperages.   Note: Users may need to supply a prefix such as ‘m' to show rates such as ‘mA/A'.  # noqa: E501, E741, RUF003
    VPerVA = "VPerVA"  # Power factor, PF, the ratio of the active power to the apparent power.  Note: The sign convention used for power factor will differ between IEC meters and EEI (ANSI) meters. It is assumed that the data consumers understand the type of meter being used and agree on the sign convention in use at any given utility.  # noqa: E501, E741, RUF003
    rev = "rev"  # Amount of rotation, revolutions.  # noqa: E501, E741, RUF003
    kat = "kat"  # Catalytic activity, katal = mol / s.  # noqa: E501, E741, RUF003
    JPerkg = "JPerkg"  # Specific energy, Joules / kg.  # noqa: E501, E741, RUF003
    m3Uncompensated = "m3Uncompensated"  # Volume, cubic metres, with the value uncompensated for weather effects.  # noqa: E501, E741, RUF003
    m3Compensated = "m3Compensated"  # Volume, cubic metres, with the value compensated for weather effects.  # noqa: E501, E741, RUF003
    WPerW = "WPerW"  # Signal Strength, ratio of power.   Note: Users may need to supply a prefix such as ‘m' to show rates such as ‘mW/W'.  # noqa: E501, E741, RUF003
    therm = "therm"  # Energy, therms.  # noqa: E501, E741, RUF003
    onePerm = "onePerm"  # Wavenumber, reciprocal metres,  (1/m).  # noqa: E501, E741, RUF003
    m3Perkg = "m3Perkg"  # Specific volume, cubic metres per kilogram, v.  # noqa: E501, E741, RUF003
    Pas = "Pas"  # Dynamic viscosity, pascal seconds.  # noqa: E501, E741, RUF003
    Nm = "Nm"  # Moment of force, newton metres.  # noqa: E501, E741, RUF003
    NPerm = "NPerm"  # Surface tension, newton per metre.  # noqa: E501, E741, RUF003
    radPers2 = "radPers2"  # Angular acceleration, radians per second squared.  # noqa: E501, E741, RUF003
    JPerm3 = "JPerm3"  # Energy density, joules per cubic metre.  # noqa: E501, E741, RUF003
    VPerm = "VPerm"  # Electric field strength, volts per metre.  # noqa: E501, E741, RUF003
    CPerm3 = "CPerm3"  # Electric charge density, coulombs per cubic metre.  # noqa: E501, E741, RUF003
    CPerm2 = "CPerm2"  # Surface charge density, coulombs per square metre.  # noqa: E501, E741, RUF003
    FPerm = "FPerm"  # Permittivity, farads per metre.  # noqa: E501, E741, RUF003
    HPerm = "HPerm"  # Permeability, henrys per metre.  # noqa: E501, E741, RUF003
    JPermol = "JPermol"  # Molar energy, joules per mole.  # noqa: E501, E741, RUF003
    JPermolK = "JPermolK"  # Molar entropy, molar heat capacity, joules per mole kelvin.  # noqa: E501, E741, RUF003
    CPerkg = "CPerkg"  # Exposure (x rays), coulombs per kilogram.  # noqa: E501, E741, RUF003
    GyPers = "GyPers"  # Absorbed dose rate, grays per second.  # noqa: E501, E741, RUF003
    WPersr = "WPersr"  # Radiant intensity, watts per steradian.  # noqa: E501, E741, RUF003
    WPerm2sr = "WPerm2sr"  # Radiance, watts per square metre steradian.  # noqa: E501, E741, RUF003
    katPerm3 = "katPerm3"  # Catalytic activity concentration, katals per cubic metre.  # noqa: E501, E741, RUF003
    d = "d"  # Time in days, day = 24 h = 86400 s.  # noqa: E501, E741, RUF003
    anglemin = "anglemin"  # Plane angle, minutes.  # noqa: E501, E741, RUF003
    anglesec = "anglesec"  # Plane angle, seconds.  # noqa: E501, E741, RUF003
    ha = "ha"  # Area, hectares.  # noqa: E501, E741, RUF003
    tonne = "tonne"  # Mass in tons, &quot;tonne&quot; or &quot;metric  ton&quot; (1000 kg = 1 Mg).  # noqa: E501, E741, RUF003
    bar = "bar"  # Pressure in bars, (1 bar = 100 kPa).  # noqa: E501, E741, RUF003
    mmHg = "mmHg"  # Pressure, millimetres of mercury (1 mmHg is approximately 133.3 Pa).  # noqa: E501, E741, RUF003
    M = "M"  # Length, nautical miles (1 M = 1852 m).  # noqa: E501, E741, RUF003
    kn = "kn"  # Speed, knots (1 kn = 1852/3600) m/s.  # noqa: E501, E741, RUF003
    Mx = "Mx"  # Magnetic flux, maxwells (1 Mx = 10-8 Wb).  # noqa: E501, E741, RUF003
    G = "G"  # Magnetic flux density, gausses (1 G = 10-4 T).  # noqa: E501, E741, RUF003
    Oe = "Oe"  # Magnetic field in oersteds, (1 Oe = (103/4p) A/m).  # noqa: E501, E741, RUF003
    Vh = "Vh"  # Volt-hour, Volt hours.  # noqa: E501, E741, RUF003
    WPerA = "WPerA"  # Active power per current flow, watts per Ampere.  # noqa: E501, E741, RUF003
    onePerHz = "onePerHz"  # Reciprocal of frequency (1/Hz).  # noqa: E501, E741, RUF003
    VPerVAr = "VPerVAr"  # Power factor, PF, the ratio of the active power to the apparent power. Note: The sign convention used for power factor will differ between IEC meters and EEI (ANSI) meters. It is assumed that the data consumers understand the type of meter being used and agree on the sign convention in use at any given utility.  # noqa: E501, E741, RUF003
    ohmPerm = "ohmPerm"  # Electric resistance per length in ohms per metre ((V/A)/m).  # noqa: E501, E741, RUF003
    kgPerJ = "kgPerJ"  # Weight per energy in kilograms per joule (kg/J). Note: multiplier &quot;k&quot; is included in this unit symbol for compatibility with IEC 61850-7-3.  # noqa: E501, E741, RUF003
    JPers = "JPers"  # Energy rate in joules per second (J/s).  # noqa: E501, E741, RUF003
