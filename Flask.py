增加mysql权限

grant all on *.* to hadoop@"%" identified by "hadoop";
flush privileges; (刷新系统权限表)



if __main__ = '__main__'
    #通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    #启动flask程序
    app.run()


配置文件
app.config.from_pyfile(config.cfg)

class Config(object):
    DEBUG = True 
    ITCAST = "PYTHON"

app.config["ITCAST"] = "ABC"
app.config.get("ITCAST")

#启动参数配置
app.run(host="0.0.0.0",port=5000)  
0.0.0.0代表主机IP

#访问方式
@app.route("/post_only",methods=["POST"])
默认是GET  methods=["GET","POST"] 


@app.route("\login")
def login():
    #使用url_for函数，通过视图函数的名字找到视图对应的url路径
    url = url_for("index")
    return redirect(url)


#转换器 
# 127.0.0.1:5000/goods/123
# 类型 int float path(接受斜线/),不加转换器类型，默认字符串规则（除了/的字符），也可以以类的方式定义转换器（引入 werkzeug.routing模块的BaseConverter)
@app.route("/goods/<int:goods_id>")
def goods_detail(goods_id):
    return "goods %s" % goods_id


# abort 函数   from flask import abort  
#使用abort函数可以立即终止视图函数的执行，并可以返回给前端特定的信息
# 传递状态码 abort(404)
# 传递响应体信息


#定义错误处理方法
@app.errorhandler(404)
def handle_404_error(err):
    """自定义的错误处理方法"""
    #返回值是前端用户看到的最终结果
    return u"出现了404错误，错误信息： %s" % err 


# json.dumps(字典)  将python字典转换为字符串
# json.loads(字符串) 将字符串转换为python中的字典
# jsonify帮助转为json数据，并设置响应头 Content-type 为application/json
# return jsonify(data)
return jsonify(city="sz", contry="china")


# cookie的设置与删除
@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    # 设置cookie,默认有效期是临时cookie，浏览器关闭就失效
    resp.set_cookie("Itcast", "python")
    # 通过max_age设置有效期，单位秒
    resp.set_cookie("Itcast2", "python2", max_age=3600)
    return resp

@app.route("/get_cookie")
def get_cookie():
    c = resquest.cookies.get("Itcast")
    return c 

@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("Itcast2") 
    return resp 


#session 会话存放状态信息
from flask import session
#flask的session需要用到秘钥字符串
app.config["SECRET_KEYS"] = "asdfsefsgegesasewa"

@app.route("/login")
def login():
    session["name"] = "python"
    session["mobile"] = "18545674546"
    return "login seccess"

@app.route("/index")
def index():
    name = session.get("name")
    return "hello %s" % name 



