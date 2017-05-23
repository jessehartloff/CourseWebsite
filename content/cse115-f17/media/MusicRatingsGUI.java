import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;

import javax.swing.*;

public class MusicRatingsGUI {

    
    private ImageIcon getThumbnail(String youtubeID){
        String url = "https://img.youtube.com/vi/" + youtubeID + "/hqdefault.jpg";
        try {
            return new ImageIcon(new URL(url));
        } catch (MalformedURLException e) {
            e.printStackTrace();
            return new ImageIcon();
        }
    }

    
    private JPanel getPanelNorth() {
        JPanel panel = new JPanel(new BorderLayout());
        
        JComboBox<Song> songBox = new JComboBox<>();
        ArrayList<Song> goodSongs = MusicRatings.getGoodSongs(4.5, 3);
        for(Song song : goodSongs){
            songBox.addItem(song);
        }
        
        
        JButton playButton = new JButton("Play");
        playButton.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {
                Song song = songBox.getItemAt(songBox.getSelectedIndex());
                song.play();
            }
        });
        
        
        JLabel image = new JLabel();
        if(goodSongs.size() > 0){
            image.setIcon(getThumbnail(goodSongs.get(0).getYoutubeID()));
        }
        
        songBox.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {
                String id = songBox.getItemAt(songBox.getSelectedIndex()).getYoutubeID();
                image.setIcon(getThumbnail(id));
            }
        });
        


        JPanel dropdownPanel = new JPanel();
        dropdownPanel.add(songBox);
        
        JPanel imagePanel = new JPanel();
        imagePanel.add(image);
        
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(playButton);
        
        panel.add(dropdownPanel, BorderLayout.NORTH);
        panel.add(imagePanel, BorderLayout.CENTER);
        panel.add(buttonPanel, BorderLayout.SOUTH);
        
        return panel;
    }
    
    
    
    
    public static void startGUI() {
        JFrame frame = new JFrame("Music Ratings");
        frame.setSize(900, 500);
        
        MusicRatingsGUI gui = new MusicRatingsGUI();

        frame.add(gui.getPanelNorth(), BorderLayout.NORTH);
        
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    public static void main(String[] args){
        SwingUtilities.invokeLater(new Runnable(){
            @Override
            public void run() {
                startGUI();
            }
        });
    }
    
}
