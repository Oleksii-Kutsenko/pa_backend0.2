# Generated by Django 3.1.9 on 2021-06-07 15:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django_better_admin_arrayfield.models.fields
import fin.models.ticker.ticker


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('currency', models.CharField(choices=[('UAH', 'Ukrainian Hryvnia'), ('USD', 'United States Dollar'), ('EUR', 'Euro')], max_length=3)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('data_source_url', models.URLField(choices=[('https://amplifyetfs.com/Data/Feeds/ForesideAmplify.40XL.XL_Holdings.csv', 'IBUY'), ('https://www.ishares.com/us/products/239516/ishares-us-medical-devices-etf/1467271812596.ajax', 'IHI'), ('https://www.ishares.com/us/products/239724/ishares-core-sp-total-us-stock-market-etf/1467271812596.ajax', 'ITOT'), ('https://www.ishares.com/us/products/244048/ishares-core-msci-total-international-stock-etf/1467271812596.ajax', 'IXUS'), ('http://invescopowershares.com/products/overview.aspx?ticker=PBW', 'PBW'), ('https://www.ishares.com/us/products/239714/ishares-russell-3000-etf/1467271812596.ajax', 'RUSSEL3000'), ('https://www.ishares.com/us/products/239705/ishares-phlx-semiconductor-etf/1467271812596.ajax', 'SOXX')], unique=True)),
                ('status', models.IntegerField(choices=[(0, 'Successfully Updated'), (1, 'Updating'), (2, 'Update Failed')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IndexTicker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('raw_data', models.JSONField(default=dict)),
                ('weight', models.DecimalField(decimal_places=10, max_digits=19, validators=[django.core.validators.MinValueValidator(1e-06), django.core.validators.MaxValueValidator(1.000001)])),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Successfully Updated'), (1, 'Updating'), (2, 'Update Failed')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('asset_to_equity_max_ratio', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('asset_to_equity_min_ratio', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('debt_to_equity_max_ratio', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('max_dividend_payout_ratio', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('minimum_annual_earnings_growth', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('pe_quantile', models.IntegerField(default=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioTicker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(default='Unknown', max_length=100)),
                ('country', models.CharField(default='Unknown', max_length=50)),
                ('industry', models.CharField(default='Unknown', max_length=50)),
                ('market_cap', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('pe', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('sector', models.CharField(default='Unknown', max_length=50)),
                ('stock_exchange', models.CharField(default='Unknown', max_length=100)),
                ('symbol', models.CharField(max_length=100)),
            ],
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('outdated_tickers', fin.models.ticker.ticker.OutdatedTickersManager()),
            ],
        ),
        migrations.CreateModel(
            name='TickerStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(choices=[('capital_lease_obligations', 'Capital Lease Obligations'), ('net_income', 'Net Income'), ('outstanding_shares', 'Outstanding Shares'), ('price', 'Price'), ('short_term_debt', 'Short Term Debt'), ('total_assets', 'Total Assets'), ('total_long_term_debt', 'Total Long Term Debt'), ('total_revenue', 'Total Revenue'), ('total_shareholder_equity', 'Total Shareholder Equity')], max_length=50)),
                ('fiscal_date_ending', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=19)),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticker_statements', to='fin.ticker')),
            ],
        ),
        migrations.AddIndex(
            model_name='ticker',
            index=models.Index(fields=['company_name'], name='fin_ticker_company_e63386_idx'),
        ),
        migrations.AddIndex(
            model_name='ticker',
            index=models.Index(fields=['country'], name='fin_ticker_country_ce69e7_idx'),
        ),
        migrations.AddIndex(
            model_name='ticker',
            index=models.Index(fields=['industry'], name='fin_ticker_industr_fcc10f_idx'),
        ),
        migrations.AddIndex(
            model_name='ticker',
            index=models.Index(fields=['sector'], name='fin_ticker_sector_d03a15_idx'),
        ),
        migrations.AddIndex(
            model_name='ticker',
            index=models.Index(fields=['symbol'], name='fin_ticker_symbol_dcd8b8_idx'),
        ),
        migrations.AddConstraint(
            model_name='ticker',
            constraint=models.CheckConstraint(check=models.Q(price__gt=0), name='ticker_price_non_negative'),
        ),
        migrations.AddConstraint(
            model_name='ticker',
            constraint=models.UniqueConstraint(fields=('stock_exchange', 'symbol'), name='unique_stock_ex_ticker_combination'),
        ),
        migrations.AddField(
            model_name='portfolioticker',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='fin.portfolio'),
        ),
        migrations.AddField(
            model_name='portfolioticker',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_ticker', to='fin.ticker'),
        ),
        migrations.AddField(
            model_name='portfoliopolicy',
            name='portfolio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_policy', to='fin.portfolio'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='tickers',
            field=models.ManyToManyField(through='fin.PortfolioTicker', to='fin.Ticker'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='indexticker',
            name='index',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='index', to='fin.index'),
        ),
        migrations.AddField(
            model_name='indexticker',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticker', to='fin.ticker'),
        ),
        migrations.AddField(
            model_name='index',
            name='tickers',
            field=models.ManyToManyField(through='fin.IndexTicker', to='fin.Ticker'),
        ),
        migrations.AddField(
            model_name='account',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='fin.portfolio'),
        ),
        migrations.AlterUniqueTogether(
            name='tickerstatement',
            unique_together={('fiscal_date_ending', 'name', 'ticker_id')},
        ),
        migrations.AddIndex(
            model_name='portfolioticker',
            index=models.Index(fields=['portfolio'], name='fin_portfol_portfol_8f19db_idx'),
        ),
        migrations.AddIndex(
            model_name='portfolioticker',
            index=models.Index(fields=['ticker'], name='fin_portfol_ticker__44841e_idx'),
        ),
        migrations.AddIndex(
            model_name='portfolio',
            index=models.Index(fields=['name'], name='fin_portfol_name_a7ed17_idx'),
        ),
        migrations.AddIndex(
            model_name='portfolio',
            index=models.Index(fields=['user'], name='fin_portfol_user_id_b18df3_idx'),
        ),
        migrations.AddIndex(
            model_name='indexticker',
            index=models.Index(fields=['index'], name='fin_indexti_index_i_f63d2b_idx'),
        ),
        migrations.AddIndex(
            model_name='indexticker',
            index=models.Index(fields=['ticker'], name='fin_indexti_ticker__64cd02_idx'),
        ),
        migrations.AddIndex(
            model_name='indexticker',
            index=models.Index(fields=['weight'], name='fin_indexti_weight_d585d3_idx'),
        ),
        migrations.AddIndex(
            model_name='index',
            index=models.Index(fields=['data_source_url'], name='fin_index_data_so_42cbd3_idx'),
        ),
        migrations.AddIndex(
            model_name='account',
            index=models.Index(fields=['name'], name='fin_account_name_bad83d_idx'),
        ),
        migrations.AddIndex(
            model_name='account',
            index=models.Index(fields=['currency'], name='fin_account_currenc_038c9a_idx'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='cusip',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='ticker',
            name='isin',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='ticker',
            name='sedol',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.RemoveConstraint(
            model_name='ticker',
            name='unique_stock_ex_ticker_combination',
        ),
        migrations.AlterField(
            model_name='account',
            name='currency',
            field=models.CharField(choices=[('CAD', 'Canadian Dollar'), ('EUR', 'Euro'), ('UAH', 'Ukrainian Hryvnia'), ('USD', 'United States Dollar')], max_length=3),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='exante_account_id',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='StockExchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('aliases', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
            ],
        ),
        migrations.AlterField(
            model_name='ticker',
            name='stock_exchange',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fin.stockexchange'),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='stock_exchange',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fin.stockexchange'),
        ),
        migrations.AddConstraint(
            model_name='ticker',
            constraint=models.UniqueConstraint(fields=('stock_exchange', 'symbol', 'cusip', 'isin', 'sedol'), name='stock_exchange_symbol_unique'),
        ),
        migrations.AddConstraint(
            model_name='indexticker',
            constraint=models.UniqueConstraint(fields=('index_id', 'ticker_id'), name='index_ticker_unique'),
        ),
        migrations.RemoveIndex(
            model_name='index',
            name='fin_index_data_so_42cbd3_idx',
        ),
        migrations.RemoveField(
            model_name='index',
            name='data_source_url',
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_parser', models.IntegerField(choices=[(1, 'AmplifyParser'), (2, 'InvescoCSVParser'), (3, 'ISharesParser')])),
                ('name', models.CharField(max_length=100)),
                ('updatable', models.BooleanField(default=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='index',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fin.source'),
        ),
        migrations.CreateModel(
            name='ISharesSourceParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_type', models.CharField(max_length=20)),
                ('file_name', models.CharField(max_length=20)),
                ('file_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddIndex(
            model_name='index',
            index=models.Index(fields=['source'], name='fin_index_source__7c40b4_idx'),
        ),
        migrations.AlterField(
            model_name='index',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fin.source'),
        ),
        migrations.RemoveField(
            model_name='source',
            name='_parser',
        ),
        migrations.AddField(
            model_name='source',
            name='parser_name',
            field=models.CharField(choices=[('AmplifyParser', 'AmplifyParser'), ('InvescoCSVParser', 'InvescoCSVParser'), ('ISharesParser', 'ISharesParser')], default='ISharesParser', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='isharessourceparams',
            name='source',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fin.source'),
        ),
    ]
