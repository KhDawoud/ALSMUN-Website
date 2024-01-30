<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import GroupSection from "../../Components/GroupSection.svelte";
    import Media from '../../../assets/OC/Media/Media.jpg';
    import Catering from '../../../assets/OC/Catering/Catering.jpg';
    import MahmoudHelmy from '../../../assets/Heads/Mahmoud Helmy.jpg';
    import OmarGabr from '../../../assets/Heads/Omar Gabr.jpg';
    import SaraTalaat from '../../../assets/Heads/Sara Talaat.jpg';
    import Placeholder from '../../../assets/Icons/Default_pfp.svg';
    import HalaNasr from '../../../assets/Heads/Hala Nasr.jpg';
    import HeadShot from "../../Components/HeadShot.svelte";
    import SoftwareTeam from "../../../assets/OC/SoftwareTeam/SoftwareTeam.jpg";
    import Banner from '../../Components/Banner.svelte';
</script>
  
  
  <NavBar />
  
  <Banner />
  
  <main class="grid grid-flow-row grid-cols-1 space-y-5 m-5 px-3">
      <GroupSection noReadMe={true} header="Mahmoud Helmy - Head of Confrence Logistics" link={null} text="Hi Everyone, My name is Mahmoud Helmy, I am ALSMUN’S Head of Logistics. This has been such a wonderful learning experience. It has been a pleasure organizing and preparing everything for all of you. We hope this conference surpasses your expectations. I look forward to meeting all of you. I hope you enjoy this conference as much as we did creating it. " image={MahmoudHelmy} />
      <GroupSection noReadMe={true} header="Omar Gabr - Head of Aesthetics & Branding" link={null} text={"Working as the head of aesthetics and branding with the other heads for ALSMUN has been a very enjoyable experience. Although we had many ups and downs and many nights were spent managing all requirements for the media team and aiding with logistic academic procedures, ultimately working for the media team at alsmun has been very rewarding, as the branding and aesthetics part of mun conferences is often overlooked despite being equally as important as academics for delegate enjoyment. We hope you enjoy ALSMUN! "} image={OmarGabr} />
      <GroupSection noReadMe={false} header="Software Team" link="/meet/oc/softwareteam" text="Hello Everyone, we are very glad to have acted as your software and tech team throughout the course of this MUN. We have worked on many challenging tasks the biggest of which being this very website! We all have had an absolutley thrilling experience during this MUN and have reallly grown our skillsets and hope it shows through our work. Best of luck!" image={SoftwareTeam} />
      <GroupSection noReadMe={false} header="Media Team" link="/meet/oc/media" text="Working as the head of the media team for ALSMUNII was definetly one of my most interesting experiences in MUN, one that's a stark contrast to the usual formalities and academics of chairing in the academic committee or management for the organizing committee. Nonetheless, having engaging and strong media is a crucial part of MUN, and any other organization, to ensure that academics are balanced out with recreation, creativity, and engagement. The media team has worked together (and will continue to do so in the coming few days!!) to produce every last post you see on our Instagram page, and in partnership with our software team to ensure that we have maximum delegate engagement. We hope you love our upcoming posts!!" image={Media} />
      <GroupSection noReadMe={false} header="Catering Team" link='/meet/oc/catering' text={null} image={Catering} />
      
      
      <div class="space-y-2 space-x-0 md:row-span-1 md:grid md:grid-col-3 md:grid-flow-col md:space-x-2 md:space-y-0 w-75">
        <HeadShot name="Mostafa Dawoud" title="Room Setup" image={Placeholder} quote="Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Hala Nasr" title="Awards & Certificates" image={HalaNasr} quote = "Welcome to ALSMUNII! We can't wait to see you!" />
        <HeadShot name="Sara Talaat" title="Head of Merchandise" image={SaraTalaat} quote = "Welcome to ALSMUNII! We can't wait to see you!" />
      </div>
  </main>