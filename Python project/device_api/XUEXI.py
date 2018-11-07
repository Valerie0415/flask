

#对数据库的两个表之间进行查询
select user.value from user where user.uid in (select mete.uid from mete where mete.cid=1)
        select U.value,C.value from mete as M join cat as C on C.cid=M.cid join user as U on U.uid=M.uid 
        select * from products,product_series where t_book.bookTypeId=t_bookType.id;


#状态码返回

// 请求成功
{
    status: 0,
    statusInfo: '请求成功',
    data: {
        name: 'Tom',
        ag: 12
    }
}
// 请求失败
{
    status: 1,
    statusInfo: '权限不足'
    // 或者是复杂类型
    statusInfo: {
        'text': '参数错误',
        'parameters': {
            "email": "电子邮件格式不正确"
        }
    }
}


用http status code，客户端封装一个函数即可、




# if data_id not in ['id']:
        # if not request.args['id']:
        #     abort(400) 





@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)





from flask import jsonify
from . import main

@main.errorhandler(404)
def error_404(error):

    """这个handler可以catch住所有abort(404)以及找不到对应router的处理请求"""
    response = dict(status=0, message="404 Not Found")
    return jsonify(response), 404

@main.errorhandler(Exception)
def error_500(error):
    """这个handler可以catch住所有的abort(500)和raise exeception."""
    response = dict(status=0, message="500 Error")
    return jsonify(response), 400

class MyError(Exception):
    """自定义错误类"""
    pass

@main.errorhandler(MyError)
def MyErrorHandle(error):
    response = dict(status=0, message="400 Error")
    return jsonify(response), 400