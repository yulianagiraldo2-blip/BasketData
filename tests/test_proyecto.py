import unittest, sys, ast
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.juego import generar,NIVELES
class Proyecto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p=pd.read_csv(ROOT/'data/datos.csv'); cls.j=pd.read_csv(ROOT/'data/jugadores.csv')
    def test_sintaxis(self):
        for f in [ROOT/'app.py',* (ROOT/'pages').glob('*.py'),*(ROOT/'src').glob('*.py')]: ast.parse(f.read_text(encoding="utf-8"))
    def test_partidos(self):
        p=self.p; self.assertGreater(len(p),1000); self.assertTrue(p.id_partido.is_unique); self.assertFalse(p.isna().any().any()); self.assertTrue((p.puntos_totales==p.puntos_local+p.puntos_visitante).all()); self.assertTrue((p.ganador==p.local.where(p.puntos_local>p.puntos_visitante,p.visitante)).all())
    def test_jugadores(self):
        j=self.j; self.assertFalse(j.isna().any().any()); self.assertTrue(j.id_partido.isin(self.p.id_partido).all()); self.assertFalse(j.duplicated(['id_partido','id_jugador']).any()); self.assertTrue(j.minutos.gt(0).all())
    def test_juego(self):
        for nivel,(n,k,p) in NIVELES.items():
            qs=generar(self.j,nivel); self.assertEqual(len(qs),n)
            for q in qs:
                self.assertEqual(len(set(q['opciones'])),4); self.assertIn(q['respuesta'],q['opciones']); self.assertEqual(len(q['pistas']),k)
                d=self.j[(self.j.jugador==q['respuesta'])&(self.j.fecha==q['fecha'])&(self.j.equipo==q['equipo'])]
                for col,val in q['pistas'].items(): d=d[d[col]==val]
                self.assertFalse(d.empty)
    def test_filtros(self):
        p=self.p; d=p[(p.temporada==2022)&((p.local=='BOS')|(p.visitante=='BOS'))]; self.assertGreater(len(d),0); self.assertTrue(d.temporada.eq(2022).all()); self.assertTrue(p[p.temporada==-1].empty)
    def test_errores(self):
        with self.assertRaises(ValueError): generar(self.j,'otro')
        with self.assertRaises(ValueError): generar(self.j.iloc[:0],'Fácil')
if __name__=='__main__': unittest.main(verbosity=2)
