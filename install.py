import os

#update system first
os.system('sudo pacman -Syyu')

#install package from official repo and AUR
os.system('sudo pacman -S --needed - < pkglist-repo.txt')
os.system('for x in $(cat pkglist-aur.txt); do pamac build $x; done')

#change shell to zsh
os.system('chsh -s /bin/zsh')

#install oh-my-zsh and powerlevel10k
os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
os.system('git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k')

#install dotbare
os.system('git clone https://github.com/kazhala/dotbare.git $HOME/.oh-my-zsh/custom/plugins/dotbare')
