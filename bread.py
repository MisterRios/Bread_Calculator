import osfrom flask import Flask, render_templatefrom flask import requestapp = Flask(__name__)@app.route('/')def landing():    return render_template('breadcal.html')@app.route('/breadcal.html')def display():    return render_template('breadcal.html')@app.route('/breadres.html', methods = ['POST'])def bread_calculator():    flour = int(request.form['flour'])    water = int(request.form['water'])    salt = int(request.form['salt'])    yeast = int(request.form['yeast'])    if flour <= 0 or water <= 0 or salt <= 0 or yeast <= 0:        return render_template('breaderror.html')    else:        dough = flour + water + salt + yeast        flour_percent = 100        water_percent = 100 * (float(water) / float(flour))        salt_percent = 100 * (float(salt) / float(flour))        yeast_percent = 100 * (float(yeast) / float(flour))        return render_template('breadres.html', dough=dough, flour_percent=flour_percent, water_percent=water_percent, salt_percent=salt_percent, yeast_percent=yeast_percent)@app.route('/breadmaker.html')def display_breadmaker():    return render_template('Breadmaker.html')@app.route('/breadrecipe.html', methods = ['POST'])def dough_generator():    flour = int(request.form['flour'])    if flour > 0:        water = 0.65 * flour        salt = 0.02 * flour        yeast = 0.02 * flour        return render_template('breadrecipe.html', flour=flour, water=water, salt=salt, yeast=yeast)    else:        return render_template('flourerror.html')app.debug = Trueapp.run(host='0.0.0.0', port=int(os.environ['PORT']))