<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import TopicA from '../../../assets/Committees/JC/Topic1.jpg';
    import TopicB from '../../../assets/Committees/JC/Topic2.jpg';
    import InfoText from "../../Components/InfoText.svelte";
  
  
  </script>
  
  <NavBar />

  <h1 class="text-center font-bold underline text-6xl my-10"> Junior Committee </h1>
  <div class="grid grid-flow-row mx-auto space-y-8">
    <InfoText 
      image={TopicA}
      title="Water Scarcity and Ozone Depeletion"
      paragraphB=""
      paragraphA="The issue of water and ozone depletion has increased greatly in severity in the past 25 years
      with the ozone layer’s thickness decreasing a total of 5% worldwide and the access to water being
      restricted to 46% of the population. The effects of this are drastic to human health. Ozone depletion
      can cause increased amounts of UV radiation to reach the Earth which can lead to more cases of skin
      cancer, especially melanoma, considered the most fatal of all skin cancers. Water depletion leads to an
      increased amount of droughts, the effect of these on humans being malnutrition, increased risk of
      diseases and more. Severe drought can also affect air quality by making wildfires and dust storms
      more likely, increasing health risk in people already impacted by lung diseases or with heart diseases."
      link="https://drive.google.com/file/d/1_HH-BGOfTFCeybaEW_GvcGgD3FsbB4eR/view?usp=sharing"
      />

    <InfoText 
      image={TopicB}
      title="Topic 2: The Issue of Women's Rights in Iran"
      paragraphB="Iranian women have had a number of challenges related to their
      position in the community and in their careers. The percentage of women in the workforce dropped
      to 14% in 2020 from just 18% in 2019. This indicates that companies in Iran prefer to hire men over
      women, not because of ability level but because of gender. The Iranian government also supports and
      encourages the marriage of 13-year-old girls, despite the potential biological consequences of such an
      early marriage."
      paragraphA="Problems regarding human rights issues in Iran are many, however the biggest breach of human
      rights is heavily centred around the Iranian Government and their authorities that have been
      enforcing laws that strip Muslim women of their right of choice as to whether they choose to wear a
      hijab or not. Hijab, a head scarf that is worn so that no hair is shown to the public, became
      compulsory in Iran after the death of 22 year old Mahsa Amini who got arrested for not wearing her
      hijab properly and for wearing skinny jeans. This triggered a revolution which heavily opposed the
      idea of the hijab; however recently, Iran’s morality police have started doing street patrols to ensure
      all women are wearing hijabs."
      link="https://drive.google.com/file/d/1VHa7JUhDs1Byvaxe-mLhFDxWNM4GvH0F/view?usp=sharing"
      />
  </div>
  
  