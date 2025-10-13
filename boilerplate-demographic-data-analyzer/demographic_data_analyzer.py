import pandas as pd

import pandas as pd

def calculate_demographic_data():
    df = pd.read_csv('adult.data.csv')

    # 1. Número de personas por raza
    race_count = df['race'].value_counts()

    # 2. Edad promedio de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Porcentaje con licenciatura
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Educación avanzada
    advanced = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = round((df[advanced]['salary'] == '>50K').mean() * 100, 1)
    lower_edu_rich = round((df[~advanced]['salary'] == '>50K').mean() * 100, 1)

    # 5. Mínimo de horas trabajadas
    min_work_hours = df['hours-per-week'].min()

    # 6. Porcentaje de ricos que trabajan mínimo
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. País con mayor % de >50K
    country_rich_pct = (
        df[df['salary'] == '>50K']['native-country']
        .value_counts(normalize=True) /
        df['native-country'].value_counts(normalize=True)
    ).dropna()
    highest_earning_country = country_rich_pct.idxmax()
    highest_earning_country_percentage = round(country_rich_pct.max() * 100, 1)

    # 8. Ocupación más común en India para >50K
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation'].value_counts().idxmax()
    )

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }