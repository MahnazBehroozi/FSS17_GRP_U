#install.packages("tidyverse")
library(tidyverse)
library(dplyr)
library(MASS)
install.packages("matrixStats")
library(matrixStats)

trials <- read_csv("trialWithTime.csv")

boardTrials <- trials %>% filter( label == 1)
paperTrials <- trials %>% filter( label == 0)

q0 <- trials %>% filter( question == 0)
q1 <- trials %>% filter( question == 1)

p0 <- trials %>% filter( ParticipantOpinion == 0)
p1 <- trials %>% filter( ParticipantOpinion == 1)

# Welch's t-test
t.test(boardTrials$VisualIntakeDurationAverage,
       paperTrials$VisualIntakeDurationAverage,
       var.equal=FALSE)


t.test(boardTrials$TrialDuration,
       paperTrials$TrialDuration,
       paired=TRUE)

t.test(boardTrials$VisualIntakeFrequency,
       paperTrials$VisualIntakeFrequency,
       paired=TRUE)

t.test(boardTrials$VisualIntakeDurationAverage,
       paperTrials$VisualIntakeDurationAverage,
       paired=TRUE)

t.test(boardTrials$VisualIntakeDispersionAverage,
       paperTrials$VisualIntakeDispersionAverage,
       paired=TRUE)

t.test(boardTrials$SaccadeFrequency,
       paperTrials$SaccadeFrequency,
       paired=TRUE)

t.test(boardTrials$SaccadeDurationAverage,
       paperTrials$SaccadeDurationAverage,
       paired=TRUE)

t.test(boardTrials$SaccadeAmplitudeAverage,
       paperTrials$SaccadeAmplitudeAverage,
       paired=TRUE)

t.test(boardTrials$SaccadeVelocityAverage,
       paperTrials$SaccadeVelocityAverage,
       paired=TRUE)

t.test(boardTrials$SaccadeLatencyAverage,
       paperTrials$SaccadeLatencyAverage,
       paired=TRUE)

t.test(boardTrials$BlinkFrequency,
       paperTrials$BlinkFrequency,
       paired=TRUE)

t.test(boardTrials$BlinkDurationAverage,
       paperTrials$BlinkDurationAverage,
       paired=TRUE)

t.test(boardTrials$RegressionFrequency,
       paperTrials$RegressionFrequency,
       paired=TRUE)

########################################################

wilcox.test(boardTrials$TrialDuration,
       paperTrials$TrialDuration,
       alternative = "two.sided")

wilcox.test(boardTrials$VisualIntakeFrequency,
       paperTrials$VisualIntakeFrequency,
       alternative = "two.sided")

wilcox.test(boardTrials$VisualIntakeDurationAverage,
       paperTrials$VisualIntakeDurationAverage,
       alternative = "two.sided")

wilcox.test(boardTrials$VisualIntakeDispersionAverage,
       paperTrials$VisualIntakeDispersionAverage,
       alternative = "two.sided")

wilcox.test(boardTrials$SaccadeFrequency,
       paperTrials$SaccadeFrequency,
       alternative = "two.sided")

wilcox.test(boardTrials$SaccadeDurationAverage,
       paperTrials$SaccadeDurationAverage,
       alternative = "two.sided")

wilcox.test(boardTrials$SaccadeAmplitudeAverage,
       paperTrials$SaccadeAmplitudeAverage,
       alternative = "two.sided")

wilcox.test(boardTrials$SaccadeVelocityAverage,
       paperTrials$SaccadeVelocityAverage,
       alternative = "two.sided")

wilcox.test(boardTrials$SaccadeLatencyAverage,
       paperTrials$SaccadeLatencyAverage,
       alternative = "two.sided")

wilcox.test(boardTrials$BlinkFrequency,
       paperTrials$BlinkFrequency,
       alternative = "two.sided")

wilcox.test(boardTrials$BlinkDurationAverage,
       paperTrials$BlinkDurationAverage,
       alternative = "two.sided")

wilcox.test(boardTrials$RegressionFrequency,
       paperTrials$RegressionFrequency,
       alternative = "two.sided")

########################################################
wilcox.test(q0$TrialDuration,
            q1$TrialDuration,
            alternative = "two.sided")

wilcox.test(q0$VisualIntakeFrequency,
            q1$VisualIntakeFrequency,
            alternative = "two.sided")

wilcox.test(q0$VisualIntakeDurationAverage,
            q1$VisualIntakeDurationAverage,
            alternative = "two.sided")

wilcox.test(q0$VisualIntakeDispersionAverage,
            q1$VisualIntakeDispersionAverage,
            alternative = "two.sided")

wilcox.test(q0$SaccadeFrequency,
            q1$SaccadeFrequency,
            alternative = "two.sided")

wilcox.test(q0$SaccadeDurationAverage,
            q1$SaccadeDurationAverage,
            alternative = "two.sided")

wilcox.test(q0$SaccadeAmplitudeAverage,
            q1$SaccadeAmplitudeAverage,
            alternative = "two.sided")

wilcox.test(q0$SaccadeVelocityAverage,
            q1$SaccadeVelocityAverage,
            alternative = "two.sided")

wilcox.test(q0$SaccadeLatencyAverage,
            q1$SaccadeLatencyAverage,
            alternative = "two.sided")

wilcox.test(q0$BlinkFrequency,
            q1$BlinkFrequency,
            alternative = "two.sided")

wilcox.test(q0$BlinkDurationAverage,
            q1$BlinkDurationAverage,
            alternative = "two.sided")

wilcox.test(q0$RegressionFrequency,
            q1$RegressionFrequency,
            alternative = "two.sided")

########################################################
t.test(q0$TrialDuration,
       q1$TrialDuration,
       paired=TRUE)


t.test(q0$VisualIntakeFrequency,
       q1$VisualIntakeFrequency,
       paired=TRUE)

t.test(q0$VisualIntakeDurationAverage,
       q1$VisualIntakeDurationAverage,
       paired=TRUE)

t.test(q0$VisualIntakeDispersionAverage,
       q1$VisualIntakeDispersionAverage,
       paired=TRUE)

t.test(q0$SaccadeFrequency,
       q1$SaccadeFrequency,
       paired=TRUE)

t.test(q0$SaccadeDurationAverage,
       q1$SaccadeDurationAverage,
       paired=TRUE)

t.test(q0$SaccadeAmplitudeAverage,
       q1$SaccadeAmplitudeAverage,
       paired=TRUE)

t.test(q0$SaccadeVelocityAverage,
       q1$SaccadeVelocityAverage,
       paired=TRUE)

t.test(q0$SaccadeLatencyAverage,
       q1$SaccadeLatencyAverage,
       paired=TRUE)

t.test(q0$BlinkFrequency,
       q1$BlinkFrequency,
       paired=TRUE)

t.test(q0$BlinkDurationAverage,
       q1$BlinkDurationAverage,
       paired=TRUE)

t.test(q0$RegressionFrequency,
       q1$RegressionFrequency,
       paired=TRUE)
########################################################
t.test(p0$TrialDuration,
       p1$TrialDuration,
       paired=TRUE)


t.test(p0$VisualIntakeFrequency,
       p1$VisualIntakeFrequency,
       paired=TRUE)

t.test(p0$VisualIntakeDurationAverage,
       p1$VisualIntakeDurationAverage,
       paired=TRUE)

t.test(p0$VisualIntakeDispersionAverage,
       p1$VisualIntakeDispersionAverage,
       paired=TRUE)

t.test(p0$SaccadeFrequency,
       p1$SaccadeFrequency,
       paired=TRUE)

t.test(p0$SaccadeDurationAverage,
       p1$SaccadeDurationAverage,
       paired=TRUE)

t.test(p0$SaccadeAmplitudeAverage,
       p1$SaccadeAmplitudeAverage,
       paired=TRUE)

t.test(p0$SaccadeVelocityAverage,
       p1$SaccadeVelocityAverage,
       paired=TRUE)

t.test(p0$SaccadeLatencyAverage,
       p1$SaccadeLatencyAverage,
       paired=TRUE)

t.test(p0$BlinkFrequency,
       p1$BlinkFrequency,
       paired=TRUE)

t.test(p0$BlinkDurationAverage,
       p1$BlinkDurationAverage,
       paired=TRUE)

t.test(p0$RegressionFrequency,
       p1$RegressionFrequency,
       paired=TRUE)

#######################################
median(boardTrials$TrialDuration)
median(boardTrials$VisualIntakeFrequency)
median(boardTrials$VisualIntakeDurationAverage)
median(boardTrials$VisualIntakeDispersionAverage)
median(boardTrials$SaccadeFrequency)
median(boardTrials$SaccadeDurationAverage)
median(boardTrials$SaccadeAmplitudeAverage)
median(boardTrials$SaccadeVelocityAverage)
median(boardTrials$SaccadeLatencyAverage)
median(boardTrials$BlinkFrequency)
median(boardTrials$BlinkDurationAverage)
median(boardTrials$RegressionFrequency)
#####################################################
median(paperTrials$TrialDuration)
median(paperTrials$VisualIntakeFrequency)
median(paperTrials$VisualIntakeDurationAverage)
median(paperTrials$VisualIntakeDispersionAverage)
median(paperTrials$SaccadeFrequency)
median(paperTrials$SaccadeDurationAverage)
median(paperTrials$SaccadeAmplitudeAverage)
median(paperTrials$SaccadeVelocityAverage)
median(paperTrials$SaccadeLatencyAverage)
median(paperTrials$BlinkFrequency)
median(paperTrials$BlinkDurationAverage)
median(paperTrials$RegressionFrequency)

#######################################
median(q0$TrialDuration)
median(q0$VisualIntakeFrequency)
median(q0$VisualIntakeDurationAverage)
median(q0$VisualIntakeDispersionAverage)
median(q0$SaccadeFrequency)
median(q0$SaccadeDurationAverage)
median(q0$SaccadeAmplitudeAverage)
median(q0$SaccadeVelocityAverage)
median(q0$SaccadeLatencyAverage)
median(q0$BlinkFrequency)
median(q0$BlinkDurationAverage)
median(q0$RegressionFrequency)
#######################################
median(q1$TrialDuration)
median(q1$VisualIntakeFrequency)
median(q1$VisualIntakeDurationAverage)
median(q1$VisualIntakeDispersionAverage)
median(q1$SaccadeFrequency)
median(q1$SaccadeDurationAverage)
median(q1$SaccadeAmplitudeAverage)
median(q1$SaccadeVelocityAverage)
median(q1$SaccadeLatencyAverage)
median(q1$BlinkFrequency)
median(q1$BlinkDurationAverage)
median(q1$RegressionFrequency)
#####################################################



colMeans(paperTrials)
colMeans(boardTrials)
colMeans(q0)
colMeans(q1)
