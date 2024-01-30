<script lang="ts">
  import NavBar from "../../Components/NavBar.svelte";
  import GroupSection from "../../Components/GroupSection.svelte";
  import SDG from "../../../assets/Secretariat/Secretariat.jpg";
  import Banner from '../../Components/Banner.svelte';
  import AC from '../../../assets/Background/AC.jpg';
  import OC from "../../../assets/Background/OC.jpg";


</script>


<NavBar />

<Banner />

<main class="grid grid-flow-row grid-cols-1 space-y-5 m-5">
    <GroupSection noReadMe={false} header="Secretariat" link="/meet/secretariat" text="The ALSMUNII Secretariat started out as a group of 4 students who all shared a love for MUN. However, it quickly grew into a group of friends who laughed, cried and stressed over this conference together. We can honestly say that working together on this conference has been the experience of a lifetime for us all. And that we'd all go through the midnight phone calls and hour long meetings all over again. The lessons weve learned are extremely valuble and the experiences weve had have helped shape our futures and have only made us so much more passionate about this conference. We can’t wait to share ALSMUNII with you and we hope you enjoy it as much as we have." image={SDG} />
    <GroupSection noReadMe={false} header="Academic Committee" link="/meet/ac" text="The Academic Committee is the heart of the ALSMUN II conference. Made up of over 30 students, the AC had the crucial responsibility in meticulously selecting the topics up for discussion throughout the conference, along with being the ones who actually facilitate and ensure an enjoyable yet successful debate. The AC are also the main role models for all of the delegates in their committees, and set a standard of formality and diplomacy to be followed, influencing and guiding the next generation of successful delegates. We hope and encourage that everyone is able to engage in beneficial relations with their committee chairs, in order to make the most out of this enriching experience." image={AC} />
    <GroupSection noReadMe={false} header="Organising Committee" link="/meet/oc" text="Although we've had many ups and downs, moments where we seemed lost, and times where panic took over, it is with pride that we say the ALSMUN2 OC has persevered and we have been able to successfully organize Alssons first interschool MUN. Managing our delegates, finances, catering, awards, communication with directors, and conference planning has been no easy task, but these experiences have taught the whole oc team many lessons, and we hope to carry them over to future conferences too. Most importantly for this year though, we hope our organization has been successful in ensuring that delegates get the most seamless and optimized conference they can, with anything and everything they may need." image={OC}/>
</main>

