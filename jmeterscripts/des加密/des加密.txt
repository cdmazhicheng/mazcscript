//说明：使用jmater-security-1.0-SNAPSHOT.jar进行des加密和解密
//编写者：mazhicheng
//更新日期：20180510

//*********加密**********

//步骤1：引用jmater-security-1.0-SNAPSHOT.jar包
import com.jmater.lib.security.DesIVUtil;

//步骤2：创建一个叫“aaa”的加密机器
DesIVUtil aaa = new DesIVUtil();

//步骤3：确定一个你要加密的对象，这个对象名字叫“cpwd”
String cpwd = vars.get("kkcpwd");

//步骤4：加密cpwd，使用aaa机器中的encrypt方法
String cpwdString = aaa.encrypt(cpwd,"sjyt_des");

//恭喜你！cpwdString 就是你des加密后的对象


//*********解密***********

//步骤1：我们拿上面的cpwdString来解密，使用aaa机器中的decrypt
String jiemiString = aaa.decrypt(cpwdString,"sjyt_des");

//恭喜你，jiemiString 就是你des解密后的对象