//说明：使用JavaMD5.jar进行md5加密
//编写者：mazhicheng
//更新日期：20180510

//步骤1：引用JavaMD5.jar包
import com.ndktools.javamd5.*;

//步骤2：创建一个名字叫“md5”的加密机器
Mademd5 md5 = new Mademd5();

//步骤3：确定需要加密的对象，此处先叫它‘before_str’
before_str = "xxxx";

//步骤4：将before_str 通过md5加密机器加密成 after_str
String after_str = md5.toMd5(before_str);

// 恭喜你！after_str 就是加密之后的对象