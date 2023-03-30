import pickle
import json
from src.bucatarie import Bucatarie
from src.reteta import Reteta

ingrediente = [{'nume': 'oua', 'cantitate': 4},
               {'nume': 'faina', 'cantitate': 400},
               {'nume': 'lapte', 'cantitate': 500},
               {'nume': 'zahar', 'cantitate': 100},
               {'nume': 'bicarbonat', 'cantitate': 10},
               {'nume': 'praf_de_copt', 'cantitate': 30},
               {'nume': 'ulei', 'cantitate': 120}]
Tort_cu_ciocolata=[
  {"nume": "oua", "cantitate": 6},
  {"nume": "faina", "cantitate": 500},
  {"nume": "zahar", "cantitate": 200},
  {"nume": "ciocolata", "cantitate": 200}]

bucatarie= Bucatarie()

reteta=Reteta('Clatite',ingrediente)
reteta.pregatire(bucatarie)

reteta_tort=Reteta('Tort cu ciocolata', Tort_cu_ciocolata)
reteta.pregatire(bucatarie)



