from django.core.management.base import BaseCommand, CommandError
from .stock_prediction_logic.analyse import start_analysis
from home.models import stock

class Command(BaseCommand):
    def handle(self, *args, **options):
            # obj = stock.objects.get(stockSymbol = "AAPL")
            # obj.s_and_r_trend = "n"
            # obj.volume_trend='n'
            # obj.macd_trend = "na"
            # obj.volume = "127346"
            # obj.candle_pattern = 'na'
            # obj.candle_trend='na'
            # obj.rank=int(3)
            # obj.save()
            start_analysis()
        # """ Do your work here """
        # self.stdout.write('There are {} things!'.format(MyModel.objects.count()))

# def test():
    # obj = stock.objects.get(stockSymbol = "AAPL")
    # obj.s_and_r_trend = "n"
    # obj.volume_trend='n'
    # obj.macd_trend = "na"
    # obj.volume = "127346"
    # obj.candle_pattern = 'na'
    # obj.candle_trend='na'
    # obj.rank=int(3)
    # obj.save()
