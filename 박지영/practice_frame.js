import javax.swing. *;

public class MyFrame extends JFrame {
  public MyFrame() {
    setTitle("프레임 연습"); //프레임 타이틀
    setSize(300,300); //프레임 크기
    setVisible(true); //프레임 출력
  }

  public static void main(String[] args){
    MyFrame frame = new MyFrame();
  }
}
