import java.util.ArrayList;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
/**
 * 
 * Make snowfall effect to 
 * celebrate new year 2016
 * 
 * @author Icegotcha Fantasoxy
 *
 */

@SuppressWarnings("serial")
public class HappyNewYear2016 extends JFrame {

	class Snow {
		int x, y;
		int ySpeed;
		Timer animated = new Timer(50, new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				y += ySpeed;
			}
		});

		Snow(int x, int ySpeed) {
			this.x = x;
			this.ySpeed = ySpeed;
			this.y = 0;
			animated.start();
		}
	}

	class SnowsFallArea extends JPanel{
		ArrayList<Snow> Snows = new ArrayList<Snow>();
		String text = "Happy New Year 2016!";
		Font font;
		Timer createSnow;

		public SnowsFallArea() {
			try {
				font = Font.createFont(Font.TRUETYPE_FONT, getClass().getResourceAsStream("Pacifico.ttf"));
			} catch (Exception ex) {
				font = Font.decode(Font.MONOSPACED);
			}
			font = font.deriveFont(48f);
			setFont(font);

			setBackground(Color.BLACK);

			createSnow = new Timer(100, new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					Snows.add(new Snow((int) (Math.random() * getWidth()), (int)(Math.random() * 40 + 10)));
					
					for(int index = 0; index < Snows.size(); index++){
						Snow cur = Snows.get(index);
						if(cur.y > getHeight()){
							cur.animated.stop();
							Snows.remove(index);
							index--;
						}
					}
					
					repaint();
				}
			});

			createSnow.start();
		}

		public void paintComponent(Graphics g) {
			super.paintComponent(g);

			g.setColor(Color.ORANGE);
			FontMetrics fm = g.getFontMetrics();
			g.drawString(text, getWidth() / 2 - fm.stringWidth(text) / 2, getHeight() / 2 - fm.getDescent()/2);

			if (Snows.size() == 0)
				return;
			
			g.setColor(Color.CYAN);
			for (Snow sn : Snows)
				g.fillOval(sn.x, sn.y, 10, 10);

		}
	}

	public HappyNewYear2016() {
		add(new SnowsFallArea());

	}

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable(){

			@Override
			public void run() {
				JFrame frame = new HappyNewYear2016();
				frame.setTitle("Happy New Year!!!!!!!!!!!");
				frame.setSize(500,500);
				frame.setLocationRelativeTo(null);
				frame.setVisible(true);
			}});
	}

}