from flask import Flask, jsonify, render_template
app = Flask(__name__) 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm



@app.route('/')
def hello_world():
    return jsonify({'message': 'Zahra Ebrahimi'})

@app.route('/graph')
def csvViewer():
        path = './app/static/data/out.csv'
        df   = pd.read_csv(path)
        records = df.head()

        df_control = df.query('group == "control"')
        n_old=len(df_control.index)
        df_treatment = df.query('group == "treatment"')
        n_new = len(df_treatment.index)
        new_page_converted = np.random.choice([1, 0], size=len(df_treatment.index), p=[df.converted.mean(), (1-(df.converted.mean()))])
        old_page_converted = np.random.choice([1, 0], size=len(df_control.index), p=[df.converted.mean(), (1-(df.converted.mean()))])
        new_page_converted.mean() - old_page_converted.mean()
        new_page_converted = np.random.binomial(n_new, df.converted.mean(),  10000)/n_new
        old_page_converted = np.random.binomial(n_old, df.converted.mean(),  10000)/n_old
        
        convert_old = len(df_control[df_control['converted'] == 1])
        convert_new = len(df_treatment[df_treatment['converted'] == 1])
        n_old = len(df_control.index)
        n_new = len(df_treatment.index)
        z_score, p_value = sm.stats.proportions_ztest([convert_old, convert_new], [n_old, n_new], alternative='smaller')
        z_score, p_value
        if p_value >= 0.05:
            records="B is Not better than A"
        elif p_value <= 0.05:
           records="B is  better than A"
        
        return render_template('index.html', records=records)

if __name__ == "__main__":
    app.run(debuge=True)