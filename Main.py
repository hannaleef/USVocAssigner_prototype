
#Defalt modules

#Custom modules
import DataLoad
import AudPreprocess
import VocLabel
import VocAssign
import ResultViewer


num_mic = int(input("Please enter the number of the microphone channels. \n"
                    " >> "))
IDs, Data_path, Data_aud, Data_label = DataLoad.get_info(num_mic)
n_fft, hop_length = AudPreprocess.set_stft()
Data_aud = AudPreprocess.do_stft(IDs, Data_aud, n_fft, hop_length)
Data_aud = AudPreprocess.get_amplitude(IDs, Data_aud)
Data_aud = VocAssign.ratio_only_assignment(IDs, Data_aud, Data_label, hop_length)
ResultViewer.view_result(IDs, Data_aud, hop_length)