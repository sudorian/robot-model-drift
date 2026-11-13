"""Symmetric, configurable quantity tolerances and three-way classification."""
from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class Tolerances:
    mass_relative: float = 0.005
    mass_absolute: float = 0.001
    com_absolute: float = 0.0005
    inertia_relative: float = 0.01
    range_absolute: float = 0.005
    slide_range_absolute: float = 0.0005
    limit_relative: float = 0.01
    kinematic_residual: float = 0.005
    kinematic_axis_angle: float = 0.005
    scale: float = 1.0

    def __post_init__(self):
        if any(not math.isfinite(v) or v<0 for v in self.__dict__.values()) or self.scale<=0 or self.com_absolute<=0:
            raise ValueError('Tolerances must be finite and nonnegative; scale and CoM threshold must be positive')

    def close(self, a, b, quantity):
        a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
        if a.shape != b.shape or not np.all(np.isfinite(a)) or not np.all(np.isfinite(b)):
            return False
        if quantity == "com":
            return bool(np.linalg.norm(a - b) <= self.scale * self.com_absolute)
        relative, absolute = {
            "mass": (self.mass_relative, self.mass_absolute),
            "inertia": (self.inertia_relative, 0.0),
            "range": (0.0, self.range_absolute),
            "slide_range": (0.0, self.slide_range_absolute),
            "limit": (self.limit_relative, 0.0),
        }[quantity]
        return bool(np.all(np.abs(a-b) <= self.scale * np.maximum(absolute, relative * np.maximum(np.abs(a), np.abs(b)))))

    def ratio(self,a,b,quantity):
        a,b=np.asarray(a,dtype=float),np.asarray(b,dtype=float)
        if quantity=='com':
            return float(np.linalg.norm(a-b)/(self.scale*self.com_absolute))
        relative,absolute={"mass":(self.mass_relative,self.mass_absolute),"inertia":(self.inertia_relative,0),
                           "range":(0,self.range_absolute),"slide_range":(0,self.slide_range_absolute),"limit":(self.limit_relative,0)}[quantity]
        delta=np.abs(a-b);threshold=self.scale*np.maximum(absolute,relative*np.maximum(np.abs(a),np.abs(b)))
        ratios=np.divide(delta,threshold,out=np.zeros_like(delta),where=threshold!=0)
        ratios=np.where((threshold==0)&(delta>0),np.inf,ratios)
        return float(np.max(ratios))


def classify(m, s, h, quantity, tolerances=Tolerances(), documented=False):
    if s is None or m is None or h is None:
        return "unknown"
    ms = tolerances.close(m, s, quantity)
    sh = tolerances.close(s, h, quantity)
    mh = tolerances.close(m, h, quantity)
    if ms and sh:
        return "unchanged"
    if ms:
        return "STALE"
    if mh:
        return "already synced"
    if sh:
        return "documented derivation difference" if documented else "undocumented derivation difference"
    return "needs a human look"
