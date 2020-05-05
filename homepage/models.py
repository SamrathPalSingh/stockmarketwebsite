from django.db import models

# Create your models here.

class stock(models.Model):
    stockName = models.CharField(max_length = 100)
    stockSymbol = models.CharField(max_length = 7)

    CANDLE_PATTERNS = (
    ('bumar' , 'bullish marabozu' ),
    ('bemar' , 'bearish marabozu' ),
    ('st' , 'spinning top' ),
    ('d' , 'doji' ),
    ('behar' , 'bearish harami' ),
    ('beeng' , 'bearish engulfing' ),
    ('bueng' , 'bullish engulfing' ),
    ('buhar' , 'bullish harami' ),
    ('dcc' , 'dark cloud cover' ),
    ('es' , 'evening star' ),
    ('h' , 'hammer' ),
    ('hm' , 'hanging man' ),
    ('ms' , 'morning star' ),
    ('pp' , 'piercing pattern' ),
    ('ss' , 'shooting star' ),
    ('na', 'none'),
    )

    TREND = (
    ('be' , 'bearish' ),
    ('bu' , 'bullish' ),
    ('na' , 'none' ),
    )

    REVERSAL = (
    ('y' , 'yes'),
    ('n' , 'no'),
    )

    candle_pattern = models.CharField(
    max_length = 5,
    choices = CANDLE_PATTERNS,
    default = 'na',
    help_text = 'Candle Pattern',
    )

    candle_trend = models.CharField(
    max_length = 2,
    choices = TREND,
    default = 'na',
    )

    # s_and_r = models.CharField(max_length = 20, null=True)##remove

    s_and_r_trend = models.CharField(
    max_length = 2,
    choices = REVERSAL,
    default = 'n',
    )

    volume = models.CharField(max_length = 20, null = True)##remove

    volume_trend = models.CharField(
    max_length = 1,
    choices = REVERSAL,
    default = 'n',
    )

    #macd = models.CharField(max_length = 20, null= True)##remove

    macd_trend = models.CharField(
    max_length = 2,
    choices = TREND,
    default = 'na',
    )

    rank = models.IntegerField(default = int(0))

    def __str__(self):
        return(f'Stock for {self.stockName}, Symbol: {self.stockSymbol}')

    def get_absolute_url(self):
        return(reverse('stock-detail', args = [str(self.id)]))
